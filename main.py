import os
from background import keep_alive #импорт функции для поддержки работоспособности
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time
token = os.environ.get('TOKEN')

updater = Updater(token=token,
                  use_context=True)
dispatcher = updater.dispatcher

wrds = ['tiktok.com', 'instagram.com', 'русню', 'русня', 'резать','ножи','точим','точу','нож','https://t.me/+k_Z9AGYLs7g5ZGUy']


def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="гружу")


def delete_links(update, context):
     message = update.message
     if message and message.text:
         for word in wrds:
             if word in message.text:
                 time.sleep(5)
                 context.bot.delete_message(chat_id=update.effective_chat.id,
                                            message_id=update.message.message_id)
                 break  # выход из цикла после удаления первого найденного слова

start_handler = CommandHandler('start', start)
delete_handler = MessageHandler(Filters.text & (~Filters.command),
                                delete_links)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(delete_handler)

keep_alive()#запускаем flask-сервер в отдельном потоке. Подробнее ниже...

updater.start_polling()
updater.idle()
