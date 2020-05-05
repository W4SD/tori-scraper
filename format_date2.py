from datetime import datetime, timedelta



def get_datetime2(date_string):


    # time_stamp = date_string.split()
    time_stamp = date_string.split()

    if len(time_stamp) > 2:
        return datetime.today() - timedelta(hours=30)
    else:
        if time_stamp[0] == "tänään":
            date = datetime.today().day
        else:
            yesterday = datetime.today() - timedelta(days=1)
            date = yesterday.day

    month = datetime.today().month
    year = datetime.today().year
    time = time_stamp[-1]

    formatted_time_stamp = f'{date} {month} {year} {time}'
    return datetime.strptime(formatted_time_stamp, '%d %m %Y %H:%M')


# time_stamp_str1 = "tänään 10:22"
# time_stamp_str2 = "eilen 05:22"
# time_stamp_str3 = "4 tou 15:48"
#
# print(get_datetime2(time_stamp_str1))
# print(get_datetime2(time_stamp_str2))
# print(get_datetime2(time_stamp_str3))
