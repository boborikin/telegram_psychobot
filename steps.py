STEPS = {
    '1': {
        'buttons': ['Начать проработку'],
        'next': '3',
        'prev': '1'
    },
    # '2': {
    #     'buttons': ['Я Мужчина', 'Я Женщина'],
    #     'variable': 'gender',
    #     'next': '3',
    #     'prev': '1'
    # },
    '3': {
        'variable': 'rec_1',
        'next': '4',
        'prev': '1'
    },
    '4': {
        'set_variable': False,
        'next': ['4.1.2'],
        'prev': '3',
    },
    '4.1.1': {
        'buttons': ['Сопротивление действовать'],
        'next': '4.1.2',
        'prev': '3'
    },
    '4.1.2': {
        'variable': 'Nforecast_1',
        'next': '4.1.3',
        'prev': '4'
    },
    '4.1.3': {
        'variable': 'Reaction_1',
        'next': '4.1.4',
        'prev': '4.1.2'
    },
    '4.1.4': {
        # 'buttons': ['Да', 'Нет'],
        'next': '',
        'prev': '4.1.3'
    },
    '4.2.1': {
        'buttons': ['Да'],
        'next': '4.2.2',
        'prev': '4.1.4'
    },
    '4.2.2': {
        'next': '',
        'prev': '4.1.4'
    },
    '4.3.1': {
        'buttons': ['Нет'],
        'next': '4.3.2',
        'prev': '4.1.4'
    },
    '4.3.2': {
        'variable': 'Situation_2',
        'next': '4.3.3',
        'prev': '4.1.4'
    },
    '4.3.3': {
        'buttons': ['Стыд', 'Печаль', 'Неприязнь', 'Гнев', 'Страх'],
        'variable': 'Emotion_2',
        'next': '4.3.4',
        'prev': '4.3.2'
    },
    '4.3.4': {
        'variable': 'Argument_2',
        'next': '4.3.5',
        'prev': '4.3.3'
    },
    '4.3.5': {
        'variable': 'Reaction_2',
        'next': '4.3.6',
        'prev': '4.3.4'
    },
    '4.3.6': {
        'variable': 'Feeling_2',
        'next': '4.3.7',
        'prev': '4.3.5'
    },
    '4.3.7': {
        'variable': 'Pforecast_2',
        'next': '4.3.8',
        'prev': '4.3.6'
    },
    '4.4.1': {
        'buttons': ['Нет'],
        'next': '4.3.2',
        'prev': '4.3.7'
    },
    '4.4.2': {
        'buttons': ['Да'],
        'next': '4.4.3',
        'prev': '4.3.7'
    },
    '4.4.3': {
        'prev': '4.3.8'
    },
    '4.4.5': {
        'buttons': ['Да'],
        'next': '4.4.7',
        'prev': '4.4.3'
    },
    '4.4.6': {
        'buttons': ['Нет'],
        'next': '4.3.2',
        'prev': '4.4.3'
    },
    '4.4.7': {
        'variable': 'user_message',
        'next': '4.4.8',
        'prev': '4.4.3'
    },

    ##########################################
    # Негативные эмоции
    ##########################################
    '5.1.1': {
        'buttons': ['Негативные эмоции'],
        'variable': 'type_working',
        'next': '5.1.2',
        'prev': '4'
    },
    '5.1.2': {
        'variable': 'Situation_1',
        'next': '5.1.3',
        'prev': '4'
    },
    '5.1.3': {
        'buttons': ['Гнев'],
        'variable': 'Emotion_1',
        'next': '5.2.1',
        'prev': '5.1.2',
    },
    '5.1.4': {
        'buttons': ['Печаль'],
        'variable': 'Emotion_1',
        'next': '6.1.1',
        'prev': '5.1.2'
    },
    '5.1.5': {
        'buttons': ['Стыд'],
        'variable': 'Emotion_1',
        'next': '7.1.1',
        'prev': '5.1.2',
    },
    '5.1.6': {
        'buttons': ['Неприязнь'],
        'variable': 'Emotion_1',
        'next': '8.1.1',
        'prev': '5.1.2',
        },
    '5.1.7': {
        'buttons': ['Страх'],
        'variable': 'Emotion_1',
        'next': '9.1.1',
        'prev': '5.1.2',
    },

    '5.1.8': {
        'buttons': ['Ничего негативного не испытываю'],
        'next': '4',
    },
    # Ветка гнев
    '5.2.1': {
        'variable': 'Argument_1',
        'next': '5.2.2',
        'prev': '5.1.3'
    },
    '5.2.2': {
        'variable': 'Feeling_1',
        'next': '5.2.3',
        'prev': '5.2.1'
    },
    '5.2.3': {
        'variable': 'Reaction_1',
        'next': '5.2.4',
        'prev': '5.2.2'
    },
    '5.2.4': {
        'variable': 'Pforecast_1',
        'next': '5.2.5',
        'prev': '5.2.3'
    },
    '5.2.5': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '5.3.1',
        'prev': '5.2.4'
    },
    '5.2.6': {
        'buttons': ['Нет'],
        'next': '5.4.1',
        'prev': '5.2.4'
    },

    # Да

    '5.3.1': {
        'variable': 'Nforecast_1',
        'next': '5.3.2',
        'prev': '5.2.5'
    },
    '5.3.2': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '5.3.4',
        'prev': '5.3.1'
    },
    '5.3.3': {
        'buttons': ['Нет'],
        'next': '5.2.1'
    },
    '5.3.4': {
        'variable': 'Situation_2',
        'next': '5.3.5',
        'prev': '5.3.2',
    },
    '5.3.5': {
        'variable': 'Argument_2',
        'next': '5.3.6',
        'prev': '5.3.4',
    },
    '5.3.6': {
        'variable': 'Feeling_2',
        'next': '5.3.7',
        'prev': '5.3.5'
    },
    '5.3.7': {
        'variable': 'Reaction_2',
        'next': '5.3.8',
        'prev': '5.3.6'
    },
    '5.3.8': {
        'variable': 'Pforecast_2',
        'next': '5.3.8.1',
        'prev': '5.3.7'
    },
    '5.3.8.1': {
        'set_variable': False,
        'next': '5.3.9',
        'prev': '5.3.8'
    },
    '5.3.8.2': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '5.3.9',
    },
    '5.3.8.3': {
        'set_variable': False,
        'buttons': ['Нет'],
        'next': '5.3.5',
    },
    '5.3.9': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '5.3.11',
        'prev': '5.3.8.1'
    },
    '5.3.10': {
        'buttons': ['Нет'],
        'next': '5.3.4'
    },
    '5.3.11': {
        'buttons': ['Да'],
        'variable': 'Word_p',
        'next': '5.3.13',
        'prev': '5.3.9'
    },
    '5.3.11.1': {
        'end_all_synonyms_messages': True,
    },
    '5.3.11.2': {
        'buttons': ['Вспомнить другую ситуацию'],
        'next': '5.3.4'
    },
    '5.3.11.3': {
        'buttons': ['Продолжить с ситуацией'],
        'variable': 'New_Word_P',
        'next': '5.3.11'
    },
    '5.3.12': {
        'buttons': ['Нет'],
        'next': '5.3.3',
        'prev': '5.3.9'
    },
    '5.3.13': {
        'synonyms': True,
        'variable': 'Word_p',
        'next': '5.3.14',
        'prev': '5.3.11'
    },
    '5.3.14': {
        'next': '5.3.15',
        'prev': '5.3.13',
    },
    '5.3.15': {
        'set_variable': False,
        'prev': '5.3.14'
    },
    '5.3.16': {
        'buttons': ['Да'],
        'next': '5.3.18',
    },
    '5.3.17': {
        'buttons': ['Нет'],
        'next': '5.3.11'
    },
    '5.3.18': {
        'prev': '5.3.15'
    },
    '5.3.19': {
        'buttons': ['Такой же ГНЕВ и'],
        'next': '5.3.11'
    },
    '5.3.20': {
        'buttons': ['Другая эмоция'],
        'next': '5.3.21',
    },

    '5.3.21': {
        'end': True,
        'prev': '5.3.18',
    },

    '5.3.22': {
        'buttons': ['Вернуться к'],
        'next': '5.1.3',
    },

    '5.3.23': {
        'buttons': ['ГНЕВ по другой причине'],
        'next': '5.3.24',
        # 'next': '5.2.1'
    },
    '5.3.24': {
        'end': True,
        'prev': '5.3.18'
    },
    '5.3.25': {
        'buttons': ['Продолжить прорабатывать'],
        # 'next': '5.1.3',
        'next': '5.2.1'
    },
    '5.3.26': {
        'buttons': ['Ничего неприятного не чувствую'],
        'next': '5.3.27'
    },
    '5.3.27': {
        'end': True,
        'prev': '5.3.18'
    },
    '5.3.28': {
        'buttons': ['Вернуться к запросу'],
        'next': '4'
    },

    # Нет

    '5.4.1': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '5.4.3',
        'prev': '5.2.5'
    },
    '5.4.2': {
        'buttons': ['Нет'],
        'next': '5.2.1',
    },
    '5.4.3': {
        'variable': 'Situation_2',
        'next': '5.4.4',
        'prev': '5.4.1'
    },
    '5.4.4': {
        'variable': 'Argument_2',
        'next': '5.4.5',
        'prev': '5.4.3'
    },
    '5.4.5': {
        'variable': 'Reaction_2',
        'next': '5.4.6',
        'prev': '5.4.4'
    },
    '5.4.6': {
        'variable': 'Feeling_2',
        'next': '5.4.7',
        'prev': '5.4.5'
    },
    '5.4.7': {
        'variable': 'Pforecast_2',
        'next': '5.4.8',
        'prev': '5.4.6'
    },
    '5.4.8': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '5.4.10',
        'prev': '5.4.7'
    },
    '5.4.9': {
        'buttons': ['Нет'],
        'next': '5.4.4',
    },
    '5.4.10': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '5.4.12',
        'prev': '5.4.8'
    },
    '5.4.11': {
        'buttons': ['Нет'],
        'next': '5.4.3',
    },
    '5.4.12': {
        'variable': 'Word_p',
        'next': '5.4.13',
        'prev': '5.4.10'
    },
    '5.4.12.1': {
        'end_all_synonyms_messages': True,
    },
    '5.4.12.2': {
        'buttons': ['Вспомнить другую ситуацию'],
        'next': '5.4.3'
    },
    '5.4.12.3': {
        'buttons': ['Продолжить с ситуацией'],
        'variable': 'New_Word_P',
        'next': '5.4.12'
    },
    '5.4.13': {
        'synonyms': True,
        'variable': 'Word_p',
        'next': '5.4.14',
        'prev': '5.4.12'
    },
    '5.4.14': {
        'next': '5.4.15',
        'prev': '5.4.13',
    },
    '5.4.15': {
        'set_variable': False,
        'prev': '5.4.14'
    },
    '5.4.16': {
        'buttons': ['Да'],
        'next': '5.4.18',
    },
    '5.4.17': {
        'buttons': ['Нет'],
        'next': '5.4.12'
    },
    '5.4.18': {
        'prev': '5.4.15'
    },
    '5.4.19': {
        'buttons': ['Такой же ГНЕВ и'],
        'next': '5.4.12'
    },
    '5.4.20': {
        'buttons': ['Другая эмоция'],
        'next': '5.4.21',
    },
    '5.4.21': {
        'end': True,
        'prev': '5.4.18',
    },
    '5.4.22': {
        'buttons': ['Вернуться к'],
        'next': '5.1.3',
    },

    '5.4.23': {
        'buttons': ['ГНЕВ по другой причине'],
        'next': '5.4.24',
        # 'next': '5.2.1'
    },
    '5.4.24': {
        'end': True,
        'prev': '5.4.18'
    },
    '5.4.25': {
        'buttons': ['Продолжить прорабатывать'],
        # 'next': '5.1.3',
        'next': '5.2.1'
    },
    '5.4.26': {
        'buttons': ['Ничего неприятного не чувствую'],
        'next': '5.4.27'
    },
    '5.4.27': {
        'end': True,
        'prev': '5.4.18'
    },
    '5.4.28': {
        'buttons': ['Вернуться к запросу'],
        'next': '4'
    },
    ###############
    # Печаль
    ###############
    '6.1.1': {
        'set_variable': False,
        # 'next': '6.1.2',
        'prev': '5.1.2'
    },
    '6.1.2': {
        'buttons': ['От потери возможности взаимодействия'],
        'next': '6.2.1',
    },
    '6.1.3': {
        'buttons': ['По другой причине'],
        'next': '6.3.1'
    },
    '6.2.1': {
        'variable': 'Argument_1',
        'next': '6.2.2',
        'prev': '6.1.1'
    },
    '6.2.2': {
        'variable': 'Reaction_1',
        'next': '6.2.3',
        'prev': '6.2.1'
    },
    '6.2.3': {
        'variable': 'Feeling_1',
        'next': '6.2.4',
        'prev': '6.2.2'
    },
    '6.2.4': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '6.2.5',
        'prev': '6.2.3'
    },
    '6.2.4.1': {
        'buttons': ['Нет'],
        'next': '6.2.1'
    },
    '6.2.5': {
        'variable': 'Word_p',
        'next': '6.2.6',
        'prev': '6.2.4'
    },
    '6.2.5.1': {
        'end_all_synonyms_messages': True,
        'redirect_step': '6.3.5'
    },
    '6.2.6': {
        'synonyms': True,
        'variable': 'Word_p',
        'next': '6.2.7',
        'prev': '6.2.5'
    },
    '6.2.7': {
        'next': '6.2.8',
        'prev': '6.2.6',
    },
    '6.2.8': {
        'set_variable': False,
        'prev': '6.2.7'
    },
    '6.2.9': {
        'buttons': ['Да'],
        'next': '6.2.11',
    },
    '6.2.10': {
        'buttons': ['Нет'],
        'next': '6.2.5'
    },
    '6.2.11': {
        'prev': '6.2.8'
    },
    '6.2.12': {
        'buttons': ['ПЕЧАЛЬ и'],
        'next': '6.2.5'
    },
    '6.2.13': {
        'buttons': ['Другая эмоция'],
        'next': '6.2.14',
    },
    '6.2.14': {
        'end': True,
        'prev': '6.2.11',
    },
    '6.2.15': {
        'buttons': ['Вернуться к'],
        'next': '5.1.3',
    },
    '6.2.16': {
        'buttons': ['ПЕЧАЛь по другой причине'],
        'next': '6.2.17',
        # 'next': '5.2.1'
    },
    '6.2.17': {
        'end': True,
        'prev': '6.2.11'
    },
    '6.2.18': {
        'buttons': ['Продолжить прорабатывать'],
        # 'next': '5.1.3',
        'next': '6.2.1'
    },
    '6.2.19': {
        'buttons': ['Ничего неприятного не чувствую'],
        'next': '6.2.20'
    },
    '6.2.20': {
        'end': True,
        'prev': '6.2.11'
    },
    '6.2.21': {
        'buttons': ['Вернуться к запросу'],
        'next': '4'
    },
    '6.3.1': {
        'variable': 'Argument_1',
        'next': '6.3.2',
        'prev': '6.1.1'
    },
    '6.3.2': {
        'variable': 'Reaction_1',
        'next': '6.3.3',
        'prev': '6.3.1'
    },
    '6.3.3': {
        'variable': 'Feeling_1',
        'next': '6.3.4',
        'prev': '6.3.2'
    },
    '6.3.4': {
        'variable': 'Pforecast_1',
        'next': '6.3.5',
        'prev': '6.3.3'
    },
    '6.3.5': {
        'variable': 'Nforecast_1',
        'next': '6.3.6',
        'prev': '6.3.4'
    },
    '6.3.6': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '6.3.8',
        'prev': '6.3.5'
    },
    '6.3.7': {
        'buttons': ['Нет'],
        'next': '6.3.1'
    },
    '6.3.8': {
        'variable': 'Situation_2',
        'next': '6.3.9',
        'prev': '6.3.6'
    },
    '6.3.9': {
        'variable': 'Argument_2',
        'next': '6.3.10',
        'prev': '6.3.8'
    },
    '6.3.10': {
        'variable': 'Reaction_2',
        'next': '6.3.11',
        'prev': '6.3.9'
    },
    '6.3.11': {
        'variable': 'Feeling_2',
        'next': '6.3.12',
        'prev': '6.3.10'
    },
    '6.3.12': {
        'variable': 'Pforecast_2',
        'next': '6.3.13',
        'prev': '6.3.11'
    },
    '6.3.13': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '6.3.15',
        'prev': '6.3.12'
    },
    '6.3.14': {
        'buttons': ['Нет'],
        'next': '6.3.9'
    },
    '6.3.15': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '6.3.17',
        'prev': '6.3.13'
    },
    '6.3.16': {
        'buttons': ['Нет'],
        'next': '6.3.8'
    },
    '6.3.17': {
        'variable': 'Word_p',
        'next': '6.3.18',
        'prev': '6.3.15'
    },####
    '6.3.17.1': {
        'end_all_synonyms_messages': True,
    },####
    '6.3.17.2': {
        'buttons': ['Вспомнить другую ситуацию'],
        'next': '6.3.8'
    },####
    '6.3.17.3': {
        'buttons': ['Продолжить с ситуацией'],
        'variable': 'New_Word_P',
        'next': '6.3.17'
    },
    '6.3.18': {
        'synonyms': True,
        'variable': 'Word_p',
        'next': '6.3.19',
        'prev': '6.3.17'
    },
    '6.3.19': {
        'next': '6.3.20',
        'prev': '6.3.18',
    },
    '6.3.20': {
        'set_variable': False,
        'prev': '6.3.19'
    },
    '6.3.21': {
        'buttons': ['Да'],
        'next': '6.3.23',
    },
    '6.3.22': {
        'buttons': ['Нет'],
        'next': '6.3.17'
    },
    '6.3.23': {
        'prev': '6.3.20'
    },
    '6.3.24': {
        'buttons': ['ПЕЧАЛЬ и'],
        'next': '6.3.17'
    },
    '6.3.25': {
        'buttons': ['Другая эмоция'],
        'next': '6.3.26',
    },
    '6.3.26': {
        'end': True,
        'prev': '6.3.23',
    },
    '6.3.27': {
        'buttons': ['Вернуться к'],
        'next': '5.1.3',
    },

    '6.3.28': {
        'buttons': ['ПЕЧАЛь по другой причине'],
        'next': '6.3.29',
        # 'next': '5.2.1'
    },
    '6.3.29': {
        'end': True,
        'prev': '6.3.23'
    },
    '6.3.30': {
        'buttons': ['Продолжить прорабатывать'],
        # 'next': '5.1.3',
        'next': '6.3.1'
    },
    '6.3.31': {
        'buttons': ['Ничего неприятного не чувствую'],
        'next': '6.3.32'
    },
    '6.3.32': {
        'end': True,
        'prev': '6.3.23'
    },
    '6.3.33': {
        'buttons': ['Вернуться к запросу'],
        'next': '4'
    },
    ####################
    # Ветка стыда
    ####################
    '7.1.1': {
        'prev': '5.1.3',
    },
    ####################
    # Ветка неприязни
    ####################
    '8.1.1': {
        'set_variable': False,
        'prev': '5.1.3'
    },
    '8.1.1.1': {
        'buttons': ['На кого-то'],
        'next': '8.1.2'
    },
    '8.1.1.2': {
        'buttons': ['На себя'],
        'next': '8.1.1.3'
    },
    '8.1.1.3': {
        'next': '7.1.1',
        'prev': '8.1.1'
    },
    '8.1.2': {
        'variable': 'Argument_1',
        'next': '8.1.3',
        'prev': '9.1.1'
    },
    '8.1.3': {
        'variable': 'Reaction_1',
        'next': '8.1.4',
        'prev': '9.1.2'
    },
    '8.1.4': {
        'variable': 'Feeling_1',
        'next': '8.1.5',
        'prev': '8.1.3'
    },
    '8.1.5': {
        'variable': 'Pforecast_1',
        'next': '8.1.6',
        'prev': '8.1.4'
    },
    '8.1.6': {
        'set_variable': False,
        'prev': '8.1.5',
    },
    '8.1.6.1': {
        'buttons': ['Да'],
        'next': '8.1.7'
    },
    '8.1.6.2': {
        'buttons': ['Нет'],
        'next': '8.1.2'
    },
    '8.1.7': {
        'variable': 'Situation_2',
        'next': '8.1.8',
        'prev': '8.1.6'
    },
    '8.1.8': {
        'variable': 'Argument_2',
        'next': '8.1.9',
        'prev': '8.1.7'
    },
    '8.1.9': {
        'variable': 'Reaction_2',
        'next': '8.2.0',
        'prev': '8.1.8'
    },
    '8.2.0': {
        'variable': 'Feeling_2',
        'next': '8.2.1',
        'prev': '8.1.9'
    },
    '8.2.1': {
        'variable': 'Pforecast_2',
        'next': '8.2.2',
        'prev': '8.2.0'
    },
    '8.2.2': {
        'set_variable': False,
        'next': '9.1.8',
        'prev': '9.2.0'
    },
    '8.2.2.0': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '8.2.3',
        'prev': '8.2.0'
    },
    '8.2.2.1': {
        'buttons': ['Нет'],
        'next': '8.1.7',
    },
    '8.2.3': {
        'set_variable': False,
        'prev': '8.2.2'
    },
    '8.2.3.0': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '8.2.4',
        'prev': '8.2.2'
    },
    '8.2.3.1': {
        'buttons': ['Нет'],
        'next': '8.1.7',
    },
    '8.2.4': {
        'variable': 'Word_p',
        'next': '8.2.5',
        'prev': '8.2.3'
    },
    '8.2.4.1': {
        'end_all_synonyms_messages': True,
    },
    '8.2.4.2': {
        'buttons': ['Вспомнить другую ситуацию'],
        'next': '8.1.7'
    },
    '8.2.4.3': {
        'buttons': ['Продолжить с ситуацией'],
        'variable': 'New_Word_P',
        'next': '8.2.4'
    },
    '8.2.5': {
        'synonyms': True,
        'variable': 'Word_p',
        'next': '8.2.7',
        'prev': '8.2.4'
    },
    '8.2.7': {
        'next': '8.2.8',
        'prev': '8.2.5',
    },
    '8.2.8': {
        'set_variable': False,
        'prev': '8.2.7'
    },
    '8.2.8.0': {
        'buttons': ['Да'],
        'next': '8.2.9',
    },
    '8.2.8.1': {
        'buttons': ['Нет'],
        'next': '8.2.4'
    },
    '8.2.9': {
        'prev': '8.2.8'
    },
    '8.3.0': {
        'buttons': ['НЕПРИЯЗНЬ и'],
        'next': '8.2.4'
    },
    '8.3.1': {
        'buttons': ['Другая эмоция'],
        'next': '8.3.2',
    },
    '8.3.2': {
        'end': True,
        'prev': '8.2.9',
    },
    '8.3.3': {
        'buttons': ['Вернуться к'],
        'next': '5.1.3',
    },
    '8.3.4': {
        'buttons': ['НЕПРИЯЗНЬ по другой причине'],
        'next': '8.3.5',
    },
    '8.3.5': {
        'end': True,
        'prev': '8.2.9'
    },
    '8.3.6': {
        'buttons': ['Продолжить прорабатывать'],
        # 'next': '5.1.3',
        'next': '8.1.7'
    },
    '8.3.7': {
        'buttons': ['Ничего неприятного не чувствую'],
        'next': '8.3.5'
    },
    '8.3.8': {
        'end': True,
        'prev': '8.2.9'
    },
    '8.3.9': {
        'buttons': ['Вернуться к запросу'],
        'next': '4'
    },
    ####################
    # Ветка страха
    ####################
    '9.1.1': {
        'variable': 'Argument_1',
        'next': '9.1.2',
        'prev': '5.1.3'
    },
    '9.1.2': {
        'variable': 'Feeling_1',
        'next': '9.1.3',
        'prev': '9.1.1'
    },
    '9.1.3': {
        'variable': 'Nforecast_1',
        'next': '9.1.4',
        'prev': '9.1.2'
    },
    '9.1.4': {
        'variable': 'Reaction_1',
        'next': '9.1.5',
        'prev': '9.1.3'
    },
    '9.1.5': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '9.1.7',
        'prev': '9.1.4'
    },
    '9.1.6': {
        'buttons': ['Нет'],
        'next': '9.1.1',
    },
    '9.1.7': {
        'variable': 'Situation_2',
        'next': '9.1.8',
        'prev': '9.1.5'
    },
    '9.1.8': {
        'variable': 'Emotion_2',
        'next': '9.1.9',
        'prev': '9.1.7'
    },
    '9.1.9': {
        'variable': 'Argument_2',
        'next': '9.2.0',
        'prev': '9.1.8'
    },
    '9.2.0': {
        'variable': 'Reaction_2',
        'next': '9.2.1',
        'prev': '9.1.9'
    },
    '9.2.1': {
        'variable': 'Feeling_2',
        'next': '9.2.2',
        'prev': '9.2.0'
    },
    '9.2.2': {
        'set_variable': False,
        'next': '9.1.8',
        'prev': '9.2.1'
    },
    '9.2.2.0': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '9.2.3',
        'prev': '9.2.1'
    },
    '9.2.2.1': {
        'buttons': ['Нет'],
        'next': '9.1.8',
    },
    '9.2.3': {
        'set_variable': False,
        'next': '9.1.8',
        'prev': '9.2.2'
    },
    '9.2.3.0': {
        'set_variable': False,
        'buttons': ['Да'],
        'next': '9.2.4',
        'prev': '9.2.2'
    },
    '9.2.3.1': {
        'buttons': ['Нет'],
        'next': '9.1.7',
    },
    '9.2.4': {
        'variable': 'Word_p',
        'next': '9.2.5',
        'prev': '9.2.3'
    },
     '9.2.4.1': {
        'end_all_synonyms_messages': True,
    },
    '9.2.4.2': {
        'buttons': ['Вспомнить другую ситуацию'],
        'next': '9.1.7'
    },
    '9.2.4.3': {
        'buttons': ['Продолжить с ситуацией'],
        'variable': 'New_Word_P',
        'next': '9.2.4'
    },
    '9.2.5': {
        'synonyms': True,
        'variable': 'Word_p',
        'next': '9.2.7',
        'prev': '9.2.4'
    },
    '9.2.7': {
        'next': '9.2.8',
        'prev': '9.2.5',
    },
    '9.2.8': {
        'set_variable': False,
        'prev': '9.2.7'
    },
    '9.2.8.0': {
        'buttons': ['Да'],
        'next': '9.2.9',
    },
    '9.2.8.1': {
        'buttons': ['Нет'],
        'next': '9.2.4'
    },
    '9.2.9': {
        'prev': '9.2.8'
    },
    '9.3.0': {
        'buttons': ['СТРАХ и'],
        'next': '9.2.4'
    },
    '9.3.1': {
        'buttons': ['Другая эмоция'],
        'next': '9.3.2',
    },
    '9.3.2': {
        'end': True,
        'prev': '9.2.9',
    },
    '9.3.3': {
        'buttons': ['Вернуться к'],
        'next': '5.1.3',
    },
    '9.3.4': {
        'buttons': ['СТРАХ по другой причине'],
        'next': '9.3.5',
    },
    '9.3.5': {
        'end': True,
        'prev': '9.2.9'
    },
    '9.3.6': {
        'buttons': ['Продолжить прорабатывать'],
        # 'next': '5.1.3',
        'next': '9.1.7'
    },
    '9.3.7': {
        'buttons': ['Ничего неприятного не чувствую'],
        'next': '9.3.5'
    },
    '9.3.8': {
        'end': True,
        'prev': '9.2.9'
    },
    '9.3.9': {
        'buttons': ['Вернуться к запросу'],
        'next': '4'
    },
    ####################
    # Ничего из перечисленного не испытывается
    ####################

    '10': {
        'buttons': ['Ничего из перечисленного не испытывается'],
        'next': '4'
    }

}
