import json
import random
from datetime import datetime, timedelta
from itertools import dropwhile

import aiohttp
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from database import Request, User, get_reqs
from keyboards import KEYBOARDS, tg_reply_keyboard
from messages import HINTS, MESSAGES, start_message
from settings import DEVELOPER_DIALOG, REVIEWS_CHANNEL, SITE, WORDS, bot, NOT_WORD_DIALOG
from steps import STEPS


class PsixologyBot:
    STEPS = STEPS
    WORDS = WORDS

    def __init__(self, messenger: str):
        self.messenger = messenger
        self.user_agent = UserAgent().random
        self.headers = {'user-agent': self.user_agent}

    async def change_word(self, word):
        word_endings = [
            'ой', 'ый', 'ий', 'ая', 'ые', 'ыми',
            'ое', 'ее', 'ого', 'его',
            'ому', 'ему', 'ым', 'им',
            'ом', 'ем', 'ой', 'ей', 'ость', 'ости',
            'ою', 'ею', 'ую', 'юю', 'яя']
        if word[0] == '-':
            word = word[1:]
        if len(word) < 4:
            return False
        flag = False
        for end in word_endings:
            if word.endswith(end):
                flag = True
                word = word.replace(end, 'ость')
                break
        print(word, 'change word')
        if not flag:
            return False
        return word

    async def get_response(self, url: str, word: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{url}{word}', headers=self.headers) as resp:
                return await resp.text()

    async def get_synonyms(self, word):
        word = await self.change_word(word)
        print(word, 'in synonyms')
        sin = []
        if word in self.WORDS:
            sin = self.WORDS[word]
        if not sin:
            synonyms = {k: v for k, v in self.WORDS.items() if not k.startswith('-')}
            for s in synonyms:
                if len(sin) == 5:
                    break
                if word in synonyms[s]:
                    sin.append(s)
        return word, sin
    
    async def get_antonyms(self, word):
        word = await self.change_word(word)
        print(word, 'word with antonyms')
        antonym = []
        if word in self.WORDS:
            antonym = self.WORDS[f'-{word}']
        if not antonym:
            antonyms = {k: v for k, v in self.WORDS.items() if k.startswith('-')}
            for a in antonyms:
                if len(antonym) == 5:
                    break
                if word in antonyms[a]:
                    new_a = a.replace('-', '')
                    if new_a not in antonym:
                        antonym.append(new_a)
        if antonym:
            antonym = [ant for ant in antonym if ant != f'не{word}']
        return word, antonym

    async def damerau_levenshtein_distance(self, s1, s2):
        d = {}
        lenstr1 = len(s1)
        lenstr2 = len(s2)
        for i in range(-1, lenstr1 + 1):
            d[(i, -1)] = i + 1
        for j in range(-1, lenstr2 + 1):
            d[(-1, j)] = j + 1
        for i in range(lenstr1):
            for j in range(lenstr2):
                if s1[i] == s2[j]:
                    cost = 0
                else:
                    cost = 1
                d[(i, j)] = min(
                    d[(i - 1, j)] + 1,  # deletion
                    d[(i, j - 1)] + 1,  # insertion
                    d[(i - 1, j - 1)] + cost,  # substitution
                )
                if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                    # transposition
                    d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)
        return d[lenstr1 - 1, lenstr2 - 1]

    async def get_keyboard(self, name: str, user_step='0', **kwargs):
        """
            messenger: tg, vk etc.
        """
        if self.messenger == 'tg':
            if user_step == '0':
                if callable(KEYBOARDS[name]):
                    return await KEYBOARDS[name](**kwargs)
                else:
                    return await tg_reply_keyboard(KEYBOARDS[name])
            else:
                if callable(KEYBOARDS[name][user_step]):
                    return await KEYBOARDS[name][user_step](**kwargs)
                else:
                    buttons_list = KEYBOARDS[name][user_step]
                    if not buttons_list:
                        if user_step not in HINTS:
                            buttons_list = [['Назад']]
                        else:
                            buttons_list = [['Подсказка'], ['Назад']]
                        buttons_list.append(['Меню'])
                    keyboard = await tg_reply_keyboard(buttons_list)
                    return keyboard

    async def get_step_message(self, **kwargs) -> str:
        step = kwargs['step']
        if callable(MESSAGES['STEPS'][step]):
            msg = await MESSAGES['STEPS'][step](**kwargs)
            if isinstance(msg, tuple):
                if 'WORD_P_MESSAGES' not in kwargs:
                    return (msg[0], random.choice(msg[1]))
                word_p_messages = [tuple(i) for i in kwargs['WORD_P_MESSAGES']]
                diff_messages = tuple(set(msg[1]) - set(word_p_messages))
                if not diff_messages:
                    return ()
                else:
                    msg = (msg[0], random.choice(diff_messages))
            return msg
        else:
            return MESSAGES['STEPS'][step]

    async def get_user(self, user_id: int) -> bool:
        user = await User.query.where(User.telegram_id == user_id).gino.first()
        if user is None:
            user = False
        return user

    async def start_command(self, user_id: int, username: str,
                            first_name: str, last_name: str) -> tuple:
        user = await self.get_user(user_id)
        if not user:
            user = await User.create(
                telegram_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name
            )
        msg = await start_message(user.first_name)
        keyboard = await self.get_keyboard('start_keyboard')
        return msg, keyboard

    async def delete_key_in_state(self, state: dict, k: str):
        if k in state:
            state = {key: value for key,
                     value in state.items() if key != k}
        return state

    async def realize_command(self, user_id: int) -> tuple:
        # Команда "Осознаю"
        # Команда "Меню"
        user = await self.get_user(user_id)
        if user:
            msg = MESSAGES['realize']
            keyboard = await self.get_keyboard('realize_keyboard', **user.state)
            state = user.state
            state['menu'] = True
            state = await self.delete_key_in_state(state, 'tips')
            state = await self.delete_key_in_state(state, 'feedback')
            await user.update(state=state).apply()
            return msg, keyboard

    async def thanks_command(self, user_id: int):
        # Команда "Как отблагодарить"
        user = await self.get_user(user_id)
        if user:
            try:
                index_step, step = await self.get_step(user.state)
                if 'end' in step:
                    if step['end']:
                        await user.update(state={'menu': True}).apply()
            except KeyError:
                pass
            msg = MESSAGES['HOW_THANKS']
            keyboard = await self.get_keyboard('how_thanks_keyboard')
            return msg, keyboard

    async def statistic_command(self, user_id: int):
        # Кнопка "Статистика"
        user = await self.get_user(user_id)
        if user:
            reqs, count_reqs = await get_reqs(user.id)
            msg = "<b>Ваша статистика:</b>\n\n"
            if reqs:
                for index, req in enumerate(reqs, start=1):
                    if req.word_p is not None \
                            and req.emotion is not None \
                            and req.situation is not None:
                        msg += f'{index}. {req.word_p} / {req.emotion} / {req.situation}\n'
            else:
                msg += 'У вас нет успешных сессий\n'
            msg += f'\n<b>Количество удачных сессий всех пользователей:</b> <code>{count_reqs}</code>'
            keyboard = await self.get_keyboard('statistic_keyboard')
            return msg, keyboard

    async def delete_user_statistic_command(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            await Request.delete.where(Request.user_id == user.id).gino.status()
            msg = MESSAGES['DELETE_USER_STATISTIC']
            keyboard = await self.get_keyboard('realize_keyboard', **user.state)
            return msg, keyboard

    async def manual_command(self, user_id):
        user = await self.get_user(user_id)
        if user:
            msg = MESSAGES['MANUAL']
            keyboard = await self.get_keyboard('manual_keyboard')
            return msg, keyboard

    async def what_is_donat_command(self, user_id: int):
        #  Команда "Что такое донэйшен"
        user = await self.get_user(user_id)
        if user:
            msg = MESSAGES['WHAT_IS_DONAT']
            return msg

    async def support_resistance_command(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            msg = MESSAGES['SUPPORT_RESISTANCE']
            keyboard = await self.get_keyboard('support_resistance_keyboard')
            return msg, keyboard

    async def about_psychotechnisc(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            msg = MESSAGES['ABOUT_PSYCHOTECHNICS']
            keyboard = await self.get_keyboard('about_psychotechnics_keyboard')
            return msg, keyboard

    async def specialist_no(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            if user.state['menu']:
                msg = MESSAGES['SPECIALIST_NO']
                return msg

    async def share_friends_command(self, user_id: int, bot_username: str):
        user = await self.get_user(user_id)
        if user:
            msg = f'{MESSAGES["SHARE_FRIENDS"]} <a href="https://t.me/{bot_username}">https://t.me/{bot_username}</a>'
            return msg

    async def write_sum_command(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            state = user.state
            state['tips'] = 'writing'
            msg = MESSAGES['WRITE_SUM']
            keyboard = await self.get_keyboard('write_sum_keyboard')
            await user.update(state=state).apply()
            return msg, keyboard

    async def set_sum_command(self, user_id: int, tips: str):
        user = await self.get_user(user_id)
        if user:
            try:
                tips = int(tips)
                msg = MESSAGES['SET_SUM']
                keyboard = await self.get_keyboard('set_sum_keyboard')
                state = user.state
                state['tips'] = tips
                await user.update(state=state).apply()
            except ValueError:
                msg = MESSAGES['WRITE_SUM']
                keyboard = await self.get_keyboard('write_sum_keyboard')
            return msg, keyboard

    async def reviews_command(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            msg = MESSAGES['REVIEWS']
            keyboard = await self.get_keyboard('reviews_keyboard')
            return msg, keyboard

    async def see_reviews_command(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            msg = f'Отзывы о боте вы можете посмотреть в нашем канале {REVIEWS_CHANNEL}'
            keyboard = await self.get_keyboard('see_reviews_channel_keyboard')
            return msg, keyboard

    async def give_reviews_command(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            msg = MESSAGES['GIVE_REVIEWS']
            keyboard = await self.get_keyboard('give_reviews_keyboard')
            state = user.state
            state['feedback'] = ''
            await user.update(state=state).apply()
            return msg, keyboard

    async def format_review_text(self, user: User, text: str):
        now_date = datetime.utcnow() + timedelta(hours=3)
        str_now_date = now_date.strftime('%d/%m/%Y')
        name = user.first_name
        return f'<b>{str_now_date} {name}:</b>\n\n{text}'

    async def set_reviews_command(self, user_id: int, text: str):
        user = await self.get_user(user_id)
        if user:
            msg = MESSAGES['SET_REVIEWS']
            keyboard = await self.get_keyboard('set_reviews_channel_keyboard', **user.state)
            review_text = await self.format_review_text(user, text)
            state = user.state
            state = await self.delete_key_in_state(state, 'feedback')
            await user.update(state=state).apply()
            return msg, keyboard, review_text

    async def feedback_command(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            msg = MESSAGES['FEEDBACK']
            keyboard = await self.get_keyboard('feedback_keyboard')
            return msg, keyboard

    async def developer_command(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            msg = f'Диалог с разработчиком: {DEVELOPER_DIALOG}'
            return msg

    async def site_command(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            msg = f'Наш сайт: <a href="{SITE}">{SITE}</a>'
            return msg

    async def session_specialist_command(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            msg = MESSAGES['SESSION_SPECIALIST']
            keyboard = await self.get_keyboard('session_specialist_keyboard')
            return msg, keyboard

    async def start_working(self, user_id: int, text: str):
        # Начать проработку
        user = await self.get_user(user_id)
        if user:
            state = {'step': '1', 'menu': False}
            await user.update(state=state).apply()
            return await self.next_step_command(user_id, text)

    async def get_step(self, state: dict, text: str = '', end_synonyms_messages: bool = False):
        if end_synonyms_messages:
            STEPS = dict(
                dropwhile(lambda item: item[0] != state['step'], self.STEPS.items()))
            for step in STEPS:
                if 'end_all_synonyms_messages' in self.STEPS[step]:
                    if 'redirect_step' in self.STEPS[step]:
                        step = self.STEPS[step]['redirect_step']
                    return step, STEPS[step]
        elif text:
            STEPS = dict(
                dropwhile(lambda item: item[0] != state['step'], self.STEPS.items()))
            for step in STEPS:
                try:
                    buttons = [i.lower() for i in STEPS[step]['buttons']]
                except KeyError:
                    continue
                if text.lower() in buttons or buttons[0].lower() in text.lower():
                    return step, STEPS[step]

        else:
            return state['step'], self.STEPS[state['step']]

    async def next_step_command(self, user_id: int, text: str):
        user = await self.get_user(user_id)
        if user:
            index_step, step = await self.get_step(user.state, text)
            state = user.state
            if not state['menu']:
                state['user_id'] = user.id
                state['step'] = step['next']
                if 'variable' in step:
                    if step['variable'] == 'New_Word_P':
                        state['WORD_P_MESSAGES'] = []
                    state[step['variable']] = text
                # Обнуляем вопросы, которые задавались из списка, когда человек доходит до конца ветки
                if 'end' in self.STEPS[step['next']]:
                    state['WORD_P_MESSAGES'] = []
                keyboard = await self.get_keyboard('STEPS', user_step=step['next'], **state)
                msg = await self.get_step_message(**state)
                if isinstance(msg, tuple):
                    if not msg:
                        index_step, step = await self.get_step(user.state, end_synonyms_messages=True)
                        state['step'] = index_step
                        state['WORD_P_MESSAGES'] = []
                        keyboard = await self.get_keyboard(name='STEPS', user_step=index_step, **state)
                        msg = await self.get_step_message(**state)
                        await user.update(state=state).apply()
                        return msg, keyboard
                    print(msg[1][0], 'dsfsdfdfddf')
                    if msg[1][0]:
                        state['Word_p'] = ''
                    else:
                        state['Word_p'] = '-'
                    state['answers_not_synonyms'] = []
                    if 'WORD_P_MESSAGES' not in state:
                        state['WORD_P_MESSAGES'] = []
                    if msg[1] not in state['WORD_P_MESSAGES']:
                        state['WORD_P_MESSAGES'].append(msg[1])
                await user.update(state=state).apply()
                return msg, keyboard

    async def continue_step(self, user_id: int):
        # Продолжить прорабатывать запрос
        user = await self.get_user(user_id)
        if user:
            keyboard = await self.get_keyboard('STEPS', user_step=user.state['step'], **user.state)
            msg = await self.get_step_message(**user.state)
            state = user.state
            state['menu'] = False
            if isinstance(msg, tuple):
                if not msg:
                    index_step, step = await self.get_step(user.state, end_synonyms_messages=True)
                    state['step'] = index_step
                    keyboard = await self.get_keyboard(name='STEPS', user_step=index_step, **state)
                    msg = await self.get_step_message(**state)
                    await user.update(state=state).apply()
                    return msg, keyboard
                else:
                    if msg[1][0]:
                        state['Word_p'] = ''
                    else:
                        state['Word_p'] = '-'
                    if 'WORD_P_MESSAGES' not in state:
                        state['WORD_P_MESSAGES'] = []
                    if msg[1] not in state['WORD_P_MESSAGES']:
                        state['WORD_P_MESSAGES'].append(msg[1])
            await user.update(state=state).apply()
            return msg, keyboard

    async def back_command(self, user_id: int, syn_new_word=False):
        user = await self.get_user(user_id)
        if user:
            index_step, step = await self.get_step(user.state)
            state = user.state
            print(state)
            if not state['menu']:
                prev_step = STEPS[step['prev']]
                state['step'] = step['prev']
                if step['prev'] == '1':
                    keyboard = await self.get_keyboard('realize_keyboard')
                    msg = MESSAGES['realize']
                else:
                    if 'variable' in prev_step:  # and 'synonyms' not in prev_step:
                        if prev_step['variable'] == 'Word_p':
                            if not state['word_p_1'].startswith('-') and not syn_new_word:
                                if state['first_word'].startswith('-'):
                                    print('sdsdd')
                                    word_p1, synonyms = await self.get_antonyms(state['first_word'])
                                    print(word_p1, synonyms, 'laska')
                                    state['word_p_1'] = f'-{word_p1}' 
                                else:
                                    word_p1, synonyms = await self.get_synonyms(state['first_word'])
                                    state['word_p_1'] = f'{word_p1}'
                            if state['word_p_1'].startswith('-'):
                                word_p1 = state['word_p_1']
                                synonyms = state['synonyms']
                            else:
                                word_p1, synonyms = await self.get_synonyms(state['word_p_1'])
                            if synonyms and word_p1 is not None:
                                state['Word_p'] = state['word_p_1'].replace('-', 'не')
                                state['synonyms'] = synonyms
                    keyboard = await self.get_keyboard(name='STEPS', user_step=step['prev'], **state)
                    msg = await self.get_step_message(**state)
                    if isinstance(msg, tuple):
                        if not msg:
                            index_step, step = await self.get_step(user.state, end_synonyms_messages=True)
                            state['step'] = index_step
                            keyboard = await self.get_keyboard(name='STEPS', user_step=index_step, **state)
                            msg = await self.get_step_message(**state)
                            await user.update(state=state).apply()
                            return msg, keyboard
                        if msg[1][0]:
                            state[step['variable']] = ''
                        else:
                            state[step['variable']] = '-'
                        if 'WORD_P_MESSAGES' not in state:
                            state['WORD_P_MESSAGES'] = []
                        if msg[1] not in state['WORD_P_MESSAGES']:
                            state['WORD_P_MESSAGES'].append(msg[1])
                await user.update(state=state).apply()
        return msg, keyboard

    async def get_hint(self, user_id: int) -> str:
        user = await self.get_user(user_id)
        if user:
            if not user.state['menu']:
                step = user.state['step']
                msg = '<b>Подсказка</b>\n\n' + HINTS[step]
                return msg

    async def set_variables(self, user_id: int, text: str):
        user = await self.get_user(user_id)
        if user:
            index_step, step = await self.get_step(user.state)
            # Если нельзя заполнять переменную то не идем дальше
            if 'set_variable' in step and not step['set_variable']:
                keyboard = await self.get_keyboard('STEPS', user_step=user.state['step'], **user.state)
                msg = await self.get_step_message(**user.state)
                return msg, keyboard
            next_step = step['next']
            state = user.state
            if not state['menu']:
                state['step'] = next_step
                if 'variable' in step and 'synonyms' not in step:
                    if step['variable'] == 'Word_p':
                        print(state[step['variable']],
                              'при формировании вопроса подается')
                        if len(text.split(' ')) == 1:
                            word = state[step['variable']] + text.lower()
                            print(word, 'w')
                            if word.startswith('-'):
                                word_p1, synonyms = await self.get_antonyms(word)
                                print('antonyms')
                            else:
                                word_p1, synonyms = await self.get_synonyms(word)
                                print('synonyms')
                            print(synonyms, '|', word, word_p1)
                        else:  # Если вводят более 2 слов
                            word_p1 = None
                            synonyms = []
                        if synonyms and word_p1 is not None:
                            if state[step['variable']].startswith('-'):
                                state[step['variable']] = f'-{word_p1}'.replace('-', 'не')
                                state['word_p_1'] = f'-{word_p1}'
                                state['first_word'] = f'-{word_p1}'
                            else:
                                state[step['variable']] = f'{word_p1}'
                                state['word_p_1'] = f'{word_p1}'
                                state['first_word'] = f'{word_p1}'
                            state['answers_not_synonyms'] = []
                            state['synonyms'] = synonyms
                        else:
                            state['step'] = index_step
                            next_step = index_step
                            await bot.send_message(NOT_WORD_DIALOG, f'Нет слова в словаре: {text.lower()}')
                    else:
                        state[step['variable']] = text
                elif 'variable' in step and 'synonyms' in step:
                    if text.lower() not in state['synonyms'] + [state['Word_p']]:
                        return 'Выберите слово с помощью кнопок', None
                    # Учитывается выбор вводимого слова или выбора синонима из списка
                    state[step['variable']] = text
                    if text != state['word_p_1'].replace('-', 'не'):
                        state['word_p_1'] = text
                    print(state)
                keyboard = await self.get_keyboard(name='STEPS', user_step=next_step, **state)
                if next_step != index_step:
                    msg = await self.get_step_message(**state)
                else:
                    if 'answers_not_synonyms' not in state:
                        state['answers_not_synonyms'] = []
                    diff_answers_not_synonyms = tuple(
                        set(MESSAGES['NOT_SYNONYMS']) - set(state['answers_not_synonyms']))
                    if diff_answers_not_synonyms:
                        msg = random.choice(diff_answers_not_synonyms)
                        state['answers_not_synonyms'].append(msg)
                    else:
                        state['answers_not_synonyms'] = []
                        msg = await self.get_step_message(**state)
                        if isinstance(msg, tuple):
                            if not msg:
                                index_step, step = await self.get_step(user.state, end_synonyms_messages=True)
                                state['step'] = index_step
                                keyboard = await self.get_keyboard(name='STEPS', user_step=index_step, **state)
                                msg = await self.get_step_message(**state)
                                await user.update(state=state).apply()
                                return msg, keyboard
                            if msg[1][0]:
                                state[step['variable']] = ''
                            else:
                                state[step['variable']] = '-'
                            if 'WORD_P_MESSAGES' not in state:
                                state['WORD_P_MESSAGES'] = []
                            if msg[1] not in state['WORD_P_MESSAGES']:
                                state['WORD_P_MESSAGES'].append(msg[1])

                await user.update(state=state).apply()
                return msg, keyboard
            else:
                return None, None

    async def request_success(self, user_id: int):
        user = await self.get_user(user_id)
        if user:
            rec_1 = user.state['rec_1']
            await Request.create(name=rec_1, successful=True, user_id=user.id)
            msg, keyboard = await self.thanks_command(user_id)
            await user.update(state={}).apply()
            return msg, keyboard
