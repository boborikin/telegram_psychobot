import re

from aiogram import Dispatcher, executor, filters, types

from bot import PsixologyBot
from database import on_shutdown, on_startup
from settings import REVIEWS_CHANNEL, bot
from keyboards import see_reviews_channel_keyboard

dp = Dispatcher(bot)
pb_bot = PsixologyBot(messenger='tg')


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    msg, keyboard = await pb_bot.start_command(
        user_id, username, first_name, last_name)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Осознаю')
@dp.message_handler(text='Меню')
async def realize_handler(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.realize_command(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Начать проработку')
async def start_working(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    msg, keyboard = await pb_bot.start_working(user_id, text)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='О психотехнике ЛДОУ')
@dp.message_handler(text='О психотехнике')
async def about_psychotechnisc(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.about_psychotechnisc(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Инструкция по использованию бота')
async def about_psychotechnisc(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.manual_command(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Что такое донэйшн?')
async def what_is_donat(message: types.Message):
    user_id = message.from_user.id
    msg = await pb_bot.what_is_donat_command(user_id)
    await bot.send_message(user_id, msg)


@dp.message_handler(text='Есть сопротивление поддержать')
async def support_resistance(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.support_resistance_command(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Рассказать друзьям')
async def share_friends(message: types.Message):
    bot_info = await bot.get_me()
    bot_username = bot_info.username
    user_id = message.from_user.id
    msg = await pb_bot.share_friends_command(user_id, bot_username)
    await bot.send_message(user_id, msg)


@dp.message_handler(filters.Regexp('Нужны синонимы к .+'))
@dp.message_handler(text='Назад')
async def back_handler(message: types.Message):
    user_id = message.from_user.id
    if message.text == 'Назад':
        msg, keyboard = await pb_bot.back_command(user_id)
    else:
        msg, keyboard = await pb_bot.back_command(user_id, syn_new_word=True)
    if isinstance(msg, tuple):
        for m in msg:
            if isinstance(m, tuple):
                await bot.send_message(user_id, m[-1], reply_markup=keyboard)
            else:
                await bot.send_message(user_id, m, reply_markup=keyboard)
    else:
        await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(filters.Regexp('Продолжить прорабатывать запрос .+'))
async def continue_step(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.continue_step(user_id)
    if isinstance(msg, tuple):
        for m in msg:
            if isinstance(m, tuple):
                await bot.send_message(user_id, m[-1], reply_markup=keyboard)
            else:
                await bot.send_message(user_id, m, reply_markup=keyboard)
    else:
        await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Подсказка')
async def hint_handler(message: types.Message):
    user_id = message.from_user.id
    msg = await pb_bot.get_hint(user_id)
    await bot.send_message(user_id, msg)


@dp.message_handler(filters.Regexp('Запрос ".+" решен'))
async def request_successful_handler(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.request_success(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Как отблагодарить')
async def how_thanks_handler(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.thanks_command(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Ввести свою сумму')
async def write_sum(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.write_sum_command(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(filters.Regexp('\d{3,4} руб.'))
async def set_tips(message: types.Message):
    user_id = message.from_user.id
    tips = re.search(r'\d{3,4}', message.text).group()
    msg, keyboard = await pb_bot.set_sum_command(user_id, tips)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Статистика')
async def statistic(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.statistic_command(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Удалить статистику пользователя')
async def delete_user_statistic(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.delete_user_statistic_command(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Отзывы')
async def reviews(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.reviews_command(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Посмотреть отзывы')
async def see_reviews(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.see_reviews_command(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Оставить отзыв')
async def give_reviews(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.give_reviews_command(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Обратная связь')
async def give_reviews(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.feedback_command(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler(text='Разработчики')
async def see_reviews(message: types.Message):
    user_id = message.from_user.id
    msg = await pb_bot.developer_command(user_id)
    await bot.send_message(user_id, msg)


@dp.message_handler(text='Наш сайт')
async def site(message: types.Message):
    user_id = message.from_user.id
    msg = await pb_bot.site_command(user_id)
    await bot.send_message(user_id, msg)


@dp.message_handler(text='Записаться на сеанс со специалистом')
async def session_specialist(message: types.Message):
    user_id = message.from_user.id
    msg, keyboard = await pb_bot.session_specialist_command(user_id)
    await bot.send_message(user_id, msg, reply_markup=keyboard)


# @dp.callback_query_handler(lambda button: button.data == '/specialist_yes')
@dp.callback_query_handler(lambda button: button.data == '/specialist_no')
async def make_appointment(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    msg = await pb_bot.specialist_no(user_id)
    await bot.send_message(user_id, msg)


@dp.message_handler(text='От потери возможности взаимодействия')
@dp.message_handler(text='По другой причине')
@dp.message_handler(filters.Regexp('Продолжить с ситуацией .+'))
@dp.message_handler(text='Ничего негативного не испытываю')
@dp.message_handler(text='Ничего из перечисленного не испытывается')
@dp.message_handler(text='Другая эмоция')
@dp.message_handler(text='Вспомнить другую ситуацию')
@dp.message_handler(filters.Regexp('Вернуться к \w+'))
@dp.message_handler(filters.Regexp('Такой же ГНЕВ и .+ от .+'))
@dp.message_handler(filters.Regexp('ПЕЧАЛЬ и .+ от .+'))
@dp.message_handler(filters.Regexp('ГНЕВ по другой причине'))
@dp.message_handler(filters.Regexp('ПЕЧАЛЬ по другой причине'))
@dp.message_handler(filters.Regexp('СТРАХ по другой причине'))
@dp.message_handler(filters.Regexp('СТРАХ и .+ от .+'))
@dp.message_handler(filters.Regexp('НЕПРИЯЗНЬ по другой причине'))
@dp.message_handler(filters.Regexp('НЕПРИЯЗНЬ и .+ от .+'))
@dp.message_handler(filters.Regexp('Продолжить прорабатывать \w+'))
@dp.message_handler(filters.Regexp('Вернуться к запросу \w+'))
@dp.message_handler(text='Ничего неприятного не чувствую')
@dp.message_handler(text='Гнев')
@dp.message_handler(text='Стыд')
@dp.message_handler(text='Страх')
@dp.message_handler(text='Неприязнь')
@dp.message_handler(text='Печаль')
@dp.message_handler(text='Да')
@dp.message_handler(text='Нет')
@dp.message_handler(text='Я Мужчина')
@dp.message_handler(text='Я Женщина')
@dp.message_handler(text='Сопротивление действовать')
@dp.message_handler(text='Негативные эмоции')
@dp.message_handler(text='На кого-то')
@dp.message_handler(text='На себя')
async def step_handler(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    if text in ['Я Мужчина', 'Я Женщина']:
        variable = 'gender'
    elif text in ['Сопротивление действовать', 'Негативные эмоции']:
        variable = 'rec_1_type'
    msg, keyboard = await pb_bot.next_step_command(user_id, text)
    if isinstance(msg, tuple):
        for m in msg:
            if isinstance(m, tuple):
                await bot.send_message(user_id, m[-1], reply_markup=keyboard)
            else:
                await bot.send_message(user_id, m, reply_markup=keyboard)
    else:
        await bot.send_message(user_id, msg, reply_markup=keyboard)


@dp.message_handler()
async def text_handler(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    user = await pb_bot.get_user(user_id)
    if user:
        if 'feedback' in user.state:
            keyboard = await see_reviews_channel_keyboard()
            msg, keyboard, review_text = await pb_bot.set_reviews_command(user_id, text)
            m = await bot.send_message(user_id, msg, reply_markup=keyboard)
            return await bot.send_message(REVIEWS_CHANNEL, review_text)
        elif 'tips' in user.state:
            if user.state['tips'] == 'writing':
                msg, keyboard = await pb_bot.set_sum_command(user_id, text)
                return await bot.send_message(user_id, msg, reply_markup=keyboard)
    msg, keyboard = await pb_bot.set_variables(user_id, text)
    if msg is None and keyboard is None:
        return
    if isinstance(msg, tuple):
        for m in msg:
            if isinstance(m, tuple):
                await bot.send_message(user_id, m[-1], reply_markup=keyboard)
            else:
                await bot.send_message(user_id, m, reply_markup=keyboard)
    else:
        await bot.send_message(user_id, msg, reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(
        dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown
    )
