'''ссыдка на бота    http://t.me/Bot_Encyclopedia_Bot'''

import telebot
from telebot import types

bot = telebot.TeleBot('5359933212:AAGwKDXG2RlIY8EzDpO4vNKcXewLGBCmEZU')

@bot.message_handler(commands = ['start', 'help'])
def gl_function(message):
    '''гл функция'''

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    item_yes = types.InlineKeyboardButton(text = 'Конечно сыграю')
    item_no = types.InlineKeyboardButton(text = 'Извини, но нет')
    markup.add(item_no, item_yes)

    msg = bot.send_message(message.chat.id, f'Здравствуйте! Я - бот! Приветствую, {message.from_user.first_name}. Вы готовы сразиться со мной и помериться силой в знаниях и умениях. Предлагаю сыграть в игру. Сыграем?', reply_markup = markup)
    bot.register_next_step_handler(msg, checking_the_main_question)

def checking_the_main_question(message):
    '''проверка гл вопроса'''

    if message.text == 'Конечно сыграю':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True, row_width = 1)
        item_i = types.InlineKeyboardButton(text = 'Я буду ходить первым')
        item_no_i = types.InlineKeyboardButton(text = 'Можешь ходить первым')
        markup.add(item_i, item_no_i)

        with open('Хаматная доска.jpg', 'rb') as file:
            msg = bot.send_photo(message.chat.id, file, 'Круто, вот как будет выглядеть доска, на которой Вы будуте играть против меня. Выбирай кто будет ходить первый', reply_markup = markup)

        bot.register_next_step_handler(msg, the_first_move)

    else:

        bot.send_message(message.chat.id, 'Жаль, как захочешь сыграть,напиши мне /start и мы сыграем')

def the_first_move(message):
    '''первый ход'''

    if message.text == 'Я буду ходить первым':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
        item_button = types.InlineKeyboardButton(text = 'Ходить на клетку F3')
        markup.add(item_button)

        with open('Хаматная доска.jpg', 'rb') as file:
            msg = bot.send_photo(message.chat.id, file, 'Хорошо, ты играешь за белую команду, первый ход делается пешкой которая находится на F2, выбирай клетку на которую хочешь ходить', reply_markup = markup)

        bot.register_next_step_handler(msg, pop)

    if message.text == 'Можешь ходить первым':

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item_button = types.InlineKeyboardButton(text='Ходить на клетку F3')
        markup.add(item_button)

        msg = bot.send_message(message.chat.id, 'Хорошо, я сходил пешкой которая стояла на Е7, а теперь стоит на Е5\n ФОТО ')
        bot.send_message(message.chat.id, 'Теперь твой ход. Куда хочешь ходить пешкой которая стоит на F2, выбери из списка ниже', reply_markup = markup)
        bot.register_next_step_handler(msg, tut)

def tut(message):
    '''первый ход противника'''

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    item = types.InlineKeyboardButton(text = 'Я сделал задание')
    markup.add(item)

    msg = bot.send_message(message.chat.id, 'Постой, перед тем как сделать ход выполни задание: Печенье упаковали в пачки по 250 г. Пачки сложили в ящик в 4 слоя. Каждый слой имеет 5 рядов по 6 пачек в каждом. Выдержит ли ящик, если максимальная масса, на которую он рассчитан, равна 32 кг? Напиши ответ в группу ССЫЛКА НА ГРУППУ, а после нажмите на кнопку снизу', reply_markup = markup)
    bot.register_next_step_handler(msg, tot)

def tot(message):
    '''сходить 2 раз'''

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    item = types.InlineKeyboardButton(text = 'Сходить на H4')
    markup.add(item)

    bot.send_message(message.chat.id, 'Молодец правльно решил задание, я хожу конем которой стоял на В8, а теперь он стоит на А6 ')
    msg = bot.send_message(message.chat.id, 'А ты куда пойдешь королевой которая стоит на Е1', reply_markup = markup)
    bot.register_next_step_handler(msg, rer)

def rer(message):
    '''последних ход'''

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    item = types.InlineKeyboardButton(text = 'Я сделал задание')
    markup.add(item)

    with open('Задача.jpg', 'rb') as file:
        msg = bot.send_photo(message.chat.id, file, 'Постой, перед тем как сделать ход выполни задание. Напиши ответ в группу ССЫЛКА НА ГРУППУ, а после нажмите на кнопку снизу')

    bot.register_next_step_handler(msg, pmp)

def pop(message):
    '''выполнение первого задания'''

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    item = types.InlineKeyboardButton(text = 'Я сделал задание')
    markup.add(item)

    msg = bot.send_message(message.chat.id, 'Постой, перед тем как сделать ход выполни задание: Пол комнаты, имеющей форму прямоугольника со сторонами 7 м и 9 м, требуется покрыть паркетом из прямоугольных дощечек со сторонами 10 см и 20 см. Сколько потребуется таких дощечек? Напиши ответ в группу ССЫЛКА НА ГРУППУ, а после нажмите на кнопку снизу', reply_markup = markup)
    bot.register_next_step_handler(msg, pip)

def pip(message):
    '''сделанны 2 хода'''

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    item = types.InlineKeyboardButton(text = 'Сходить на H4')
    markup.add(item)

    msg = bot.send_message(message.chat.id, 'Молодец. Ты решил все правильно!!! Теперь делай сного свой ход. Сейчас будешь ходить королевой которая стоит на E1   ФОТО', reply_markup = markup)
    bot.send_message(message.chat.id, 'Пока я ждал твоего ответа на вопрос я уже сходил пешкой которая стоояла на Е7, а теперь стоит на Е5')
    bot.register_next_step_handler(msg, pup)

def pup(message):
    '''сделать ход королевой'''

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    item = types.InlineKeyboardButton(text = 'Я сделал задание')
    markup.add(item)

    msg = bot.send_message(message.chat.id, 'Хорошо, для того что бы сделать ход нужно решить хадачу. Задача: что легче: 1 кг ваты или 1 кг железа? Напиши ответ в группу ССЫЛКА НА ГРУППУ, а после нажмите на кнопку снизу', reply_markup = markup)
    bot.register_next_step_handler(msg, pmp)

def pmp(message):
    '''финал'''

    bot.send_message(message.chat.id, 'ФОТО    ПОЗДРАВЛЯЮ!!! Вы выйграли!!! Вы сделали шах и мат мне. Что бы начать заного напишите /start')

bot.polling()