from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# API TOKEN
with open('TOKEN') as f: TOKEN = f.readline()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(start_handler)

updater.start_polling()


