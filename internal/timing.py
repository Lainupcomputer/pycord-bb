from datetime import datetime

VERSION = "1.0.0.1"


def get_now_time(raw: bool = False):
    '''
    Gets The current Time
    :param raw: bool
    :return:
    current time formatted if raw false else datetime. Now
    '''
    now = datetime.now()  # get current date and time
    time = now.strftime("%m/%d/%Y, %H:%M:%S")
    if not raw:
        return time
    else:
        return now
