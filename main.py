import os
from background import keep_alive #импорт функции для поддержки работоспособности
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time

updater = Updater(token='6659951688:AAG8-SGWwSOrkFmzTvPMYpUBbYtInDvNwl4',
                  use_context=True)
dispatcher = updater.dispatcher

wrds = ['tiktok.com', 'instagram.com']


def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="гружу")


def delete_links(update, context):
  message = update.message
  if message and message.text and any(word in message.text for word in wrds):
    time.sleep(5)
    context.bot.delete_message(chat_id=update.effective_chat.id,
                               message_id=update.message.message_id)


start_handler = CommandHandler('start', start)
delete_handler = MessageHandler(Filters.text & (~Filters.command),
                                delete_links)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(delete_handler)

keep_alive()#запускаем flask-сервер в отдельном потоке. Подробнее ниже...

updater.start_polling()
updater.idle()
