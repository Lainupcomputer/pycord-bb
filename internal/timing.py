from datetime import datetime

VERSION = "1.0.0.2"


def get_time_sys():
    '''
    returns system writable formatted time
    :return: system writable formatted time
    '''
    now = datetime.now()  # get current date and time
    return now.strftime("%d-%m-%Y_%H-%M-%S")


def current_time():
    now = datetime.now()
    return now.strftime("%d.%m.%Y %H:%M")

