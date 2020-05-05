from datetime import datetime


def return_month(month):
    months={
        "tammikuuta":1,
        "helmikuuta":2,
        "maaliskuuta":3,
        "huhtikuuta":4,
        "toukokuuta":5,
        "kesäkuuta":6,
        "heinäkuuta":7,
        "elokuuta":8,
        "syyskuuta":9,
        "lokuuta":10,
        "marraskuuta":11,
        "joulukuuta":12
    }
    return months.get(month, "Invalid month")


def get_datetime(date_string):

    # time_stamp = "5 toukokuuta 23:02"
    time_stamp = date_string.split()
    date = time_stamp[0]
    month = return_month(time_stamp[1])
    year = datetime.today().year
    time = time_stamp[-1]

    formatted_time_stamp = f'{date} {month} {year} {time}'

    return datetime.strptime(formatted_time_stamp, '%d %m %Y %H:%M')

