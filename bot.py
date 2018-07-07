# -*- coding: utf-8 -*-
import config
import telebot
import logger
import time

# bot = telebot.TeleBot(config.token)
bot = telebot.TeleBot(config.token, threaded=False)
f = open('inn550.txt')
text=f.read()

@bot.message_handler(content_types=['text'])
def handle_text(message):

# Если пользователь отправил "привет, как тебя зовут?" отвечаем "робот я"

    if len(message.text) == 12 or len(message.text) == 10:
        if message.text in text:
                bot.send_message(message.from_user.id, 'Нельзя')
        else:
                bot.send_message(message.from_user.id, "Можно")
    else:
        bot.send_message(message.from_user.id, ' Перепроверьте вводимые цифры, ИНН строго 10 или 12 цифр')

# bot.polling()
if __name__ == '__main__':
    bot.polling(none_stop=True, timeout=0)

# while True:
#     try:
#         bot.polling(none_stop=True)
#
#     except Exception as e:
#         logger.error(e)  # или просто print(e) если у вас логгера нет,
#         # или import traceback; traceback.print_exc() для печати полной инфы
#         time.sleep(15)