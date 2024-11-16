import random

import telebot
from telebot import types
from infobase import card_desc, way, colors_array
from settings import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    """
    Запуск меню бота с вариацией выбора действий
    :param message: входящее сообщение
    :return:
    """

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🧡 Любовь и отношения')
    item2 = types.KeyboardButton('👑 Карьера и финансы')
    item3 = types.KeyboardButton('🌸 Здоровье')
    item4 = types.KeyboardButton('🎓 Саморазвитие и обучение')
    item5 = types.KeyboardButton('🎨 Творчество и хобби')
    item6 = types.KeyboardButton('😺 Друзья и окружение')
    item7 = types.KeyboardButton('Другое...')

    # 🎱🔮📿🧿

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    text = 'Приветствую тебя, {0.first_name}! '
    bot.send_message(message.chat.id, text.format(message.from_user), reply_markup=markup)



@bot.message_handler(content_types=['text'])
   def bot_message(message):
       """Команды для чата в личных сообщениях"""
       if message.chat.type == 'private':
           """Просмотр числа дня"""
           if message.text == '🧡 Любовь и отношения':
               temp_daynum = random.randint(1, 77)
               bot.send_message(message.chat.id, '✨Ваши шансы быть сегодня успешным в отношениях: ✨: ' + str(temp_daynum))
               """Просмотр аркана дня"""
           elif message.text == '👑 Карьера и финансы':
               temp_daycard = random.randint(0, 21)
               bot.send_message(message.chat.id, '✨Ваш аркан дня✨: ' + str(temp_daycard))
               bot.send_message(message.chat.id, '✨Описание вашего аркана дня✨: \n')
               img = open(way + str(temp_daycard) + '.jpeg', 'rb')
               bot.send_photo(message.chat.id, img, caption=card_desc[temp_daycard])
               """Просмотр цвета дня"""
           elif message.text == '🌸 Здоровье':
               bot.send_message(message.chat.id, '✨Благодадь витает в воздухе и насыщает тебя здоровьем! ✨: ' + str(random.choice(colors_array)))
               """Дополнительная кнопка, чтобы добавить новые функции"""
           elif message.text == '🎓 Саморазвитие и обучение':
               bot.send_message(message.chat.id, '✨Сегодня тебя ждет попутный ветер~ Вперед броздить океаны знаний! ✨: ' + str(random.choice(colors_array)))
               """Дополнительная кнопка, чтобы добавить новые функции"""
           elif message.text == '🎨 Творчество и хобби':
               bot.send_message(message.chat.id, '✨Муза посетит тебя, путник! Твори и будь знаменит! ✨: ' + str(random.choice(colors_array)))
               """Дополнительная кнопка, чтобы добавить новые функции"""
           elif message.text == '😺 Друзья и окружение':
               bot.send_message(message.chat.id, '✨Ваши друзья будут счастливы! ✨: ' + str(random.choice(colors_array)))
               """Дополнительная кнопка, чтобы добавить новые функции"""


           elif message.text == 'Другое...':
               bot.send_message(message.chat.id,
                                'Я начинающий маг, поэтому другие возможности покажу позже...\nНажмите /start и попробуйте снова✨')
           else:
               """Если пользователь ввел неверные символы, то ему бот выдаст ошибку"""
               bot.send_message(message.chat.id,
                                'Проводя различные манипуляции с магией, я перестал Вас понимать,\nнажмите /start и попробуйте снова✨')
   
               """Команды бота для групповых чатов"""
               """Описание функций одинаковое, но убрано реагирование бота на обычные сообщения"""

       if message.chat.type != 'private':
           """Просмотр числа дня"""
           if message.text == '🧡 Любовь и отношения':
               temp_daynum = random.randint(1, 77)
               bot.send_message(message.chat.id, '✨Ваши шансы быть сегодня успешным в отношениях: ✨: ' + str(temp_daynum))
               """Просмотр аркана дня"""
           elif message.text == '👑 Карьера и финансы':
               temp_daycard = random.randint(0, 21)
               bot.send_message(message.chat.id, '✨Ваш аркан дня✨: ' + str(temp_daycard))
               bot.send_message(message.chat.id, '✨Описание вашего аркана дня✨: \n')
               img = open(way + str(temp_daycard) + '.jpeg', 'rb')
               bot.send_photo(message.chat.id, img, caption=card_desc[temp_daycard])
               """Просмотр цвета дня"""
           elif message.text == '🌸 Здоровье':
               bot.send_message(message.chat.id, '✨Благодадь витает в воздухе и насыщает тебя здоровьем! ✨: ' + str(random.choice(colors_array)))
               """Дополнительная кнопка, чтобы добавить новые функции"""
           elif message.text == '🎓 Саморазвитие и обучение':
               bot.send_message(message.chat.id, '✨Сегодня тебя ждет попутный ветер~ Вперед броздить океаны знаний! ✨: ' + str(random.choice(colors_array)))
               """Дополнительная кнопка, чтобы добавить новые функции"""
           elif message.text == '🎨 Творчество и хобби':
               bot.send_message(message.chat.id, '✨Муза посетит тебя, путник! Твори и будь знаменит! ✨: ' + str(random.choice(colors_array)))
               """Дополнительная кнопка, чтобы добавить новые функции"""
           elif message.text == '😺 Друзья и окружение':
               bot.send_message(message.chat.id, '✨Ваши друзья будут счастливы! ✨: ' + str(random.choice(colors_array)))
               """Дополнительная кнопка, чтобы добавить новые функции"""

bot.polling(none_stop=True)
