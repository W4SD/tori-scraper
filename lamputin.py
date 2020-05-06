from telegram.ext import Updater, CommandHandler

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

token = '1174679995:AAGe7e33kUt69lYmJ__XPO9qxkU34Fcf9Mw'
updater = Updater(token=token, use_context=True)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()