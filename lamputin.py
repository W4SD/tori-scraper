from telegram.ext import Updater
from telegram.error import TelegramError
import logging
from scrape import get_listing_items
import json
import time
from datetime import datetime

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# API TOKEN
with open('TOKEN') as f: TOKEN = f.readline().rstrip()
# Channel ID
with open('Channel_ID') as c: CHANNEL = c.readline()

sent_message_ids = []
# Run time in UTC
run_time = '04:00:00'
time_object = datetime.strptime(run_time, '%H:%M:%S').time()

def i_am_alive(context):
    context.bot.send_message(chat_id=CHANNEL, text="I AM ALIVE!")


def delete_sent_messages(context):

    # no rate limiting in delete_message... change if someting weard happens.
    for x in sent_message_ids:
        context.bot.delete_message(chat_id=CHANNEL, message_id=x)
        # time.sleep(4)

    sent_message_ids.clear()
    print("Deleted messages!")


def photo_text(context):

    #delete old messages
    delete_sent_messages(context)

    data = json.loads(get_listing_items())
    print("Got new items to display!")
    # delete_sent_messages(context)

    # with open('json_item_test.json','r') as json_file:
    #     # load json file as python dict
    #     data = json.load(json_file)

    # for key in data:
    #     print(data[key]['title'])


    for item_id in data:
        time.sleep(4)
        # print(item_id)
        item_desc = (
            f"{data[item_id]['title']}"
            "\n"
            f"Hinta: <b>{data[item_id]['price']}</b>"
            "\n"
            f"{data[item_id]['product_link']}"
            "\n"
            f"Ilmoitusaika: {data[item_id]['time_stamp']}"
        )
        try:
            msg = context.bot.send_photo(chat_id=CHANNEL,
                                         photo=data[item_id]['image_link'],
                                         caption=item_desc,
                                         disable_notification=True,
                                         parse_mode='html',
                                         )
            sent_message_ids.append(msg['message_id'])

        except TelegramError:
            pass

    msg = context.bot.send_message(chat_id=CHANNEL,
                                   text=f"Uusia ilmoituksia: {len(sent_message_ids)}")
    sent_message_ids.append(msg['message_id'])
    print("Daily items listed!")


def main():

    updater = Updater(token=TOKEN, use_context=True)
    job_queue = updater.job_queue

    updater.start_polling()

    daily_lamps = job_queue.run_daily(photo_text,time_object)

    run_once = job_queue.run_once(i_am_alive, 0)
    run_on_start = job_queue.run_once(photo_text, 0)

    updater.idle()


if __name__ == '__main__':
    main()


