import telebot
from telebot import types

bot = telebot.TeleBot('7939166697:AAFSCxD1ruXcbmYGcO4bEFCMnVl2MyK7R7U')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать в магазин одежды Frizzy Shop!")

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Сделать заказ")
    btn2 = types.KeyboardButton("Сделать заказ с Poizon")
    markup.row(btn1)
    markup.row(btn2)
    btn3 = types.KeyboardButton("Написать отзыв")
    btn4 = types.KeyboardButton("Чат с поддержкой")
    markup.row(btn3, btn4)

    bot.send_message(message.chat.id, "Выберите итересующие вас действие:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Сделать заказ":
        bot.send_message(message.chat.id,
                         "Отправьте продавцу сообщеие с товаром из группы Frizzy Shop и укажите размер.\nПример:")
        file = open('./benzo.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Сделать заказ', url='https://t.me/LilFrizy'))
        bot.send_message(message.chat.id, "Заказать ТУТ:", reply_markup=markup)
    if message.text == "Сделать заказ с Poizon":
        bot.send_message(message.chat.id,
                         "Отправьте продавцу сообщеие с фото товара, артикул и укажите размер.\nПример:")
        file1 = open('./nike.jpg', 'rb')
        bot.send_photo(message.chat.id, file1)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Сделать заказ с Poizon', url='https://t.me/LilFrizy'))
        bot.send_message(message.chat.id, "Заказать ТУТ:", reply_markup=markup)
    if message.text == "Написать отзыв":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Отзыв', url='https://t.me/FrizzySho_Otzov_Bot'))
        bot.send_message(message.chat.id, "Написать отзыв:", reply_markup=markup)
    if message.text == "Чат с поддержкой":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Поддержка в ТГ', url='https://t.me/LilFrizy'))
        bot.send_message(message.chat.id, "Возникли вопросы? Ответим ТУТ:", reply_markup=markup)


if __name__ == "__main__":
    bot.polling(none_stop=True)
