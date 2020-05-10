from telegram.ext import Updater, CommandHandler
import logging
from scrape import get_listing_items
import json
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# API TOKEN
with open('TOKEN') as f: TOKEN = f.readline()
# Channel ID
with open('Channel_ID') as c: CHANNEL = c.readline()

sent_message_ids = []

def delete_sent_messages(context):

    for x in sent_message_ids:
        context.bot.delete_message(chat_id=CHANNEL, message_id=x)
        time.sleep(4)

    sent_message_ids.clear()


def photo_text(context):

    data = json.loads(get_listing_items())
    delete_sent_messages(context)

    # with open('json_item_test.json','r') as json_file:
    #     # load json file as python dict
    #     data = json.load(json_file)

    # for key in data:
    #     print(data[key]['title'])


    for item_id in data:
        time.sleep(4)
        print(item_id)
        item_desc = (
            f"{data[item_id]['title']} - <b>{data[item_id]['price']}</b>"
            "\n"
            f"{data[item_id]['product_link']}"
            "\n"
            f"Ilmoitusaika: {data[item_id]['time_stamp']}"
            "\n"
            f"ID: {data[item_id]['id']}"
        )
        msg = context.bot.send_photo(chat_id=CHANNEL,
                                     photo=data[item_id]['image_link'],
                                     caption=item_desc,
                                     disable_notification=True,
                                     parse_mode='html',
                                     )
        sent_message_ids.append(msg['message_id'])
        print(msg)
        if len(sent_message_ids) > 30:
            break
    print(sent_message_ids)
    delete_sent_messages(context)


def main():

    updater = Updater(token=TOKEN, use_context=True)
    job_queue = updater.job_queue

    updater.start_polling()

    job_minute = job_queue.run_once(photo_text, 0)

    updater.idle()

# run_daily
# https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.jobqueue.html

if __name__ == '__main__':
    main()


