"""
This File contains all internal relevant Classes and functions

"""
import os
import logging
import sys
from datetime import datetime
from colorama import Fore


def check_create_dir(path: str) -> None:
    """
    checks if a folder is on given path, if not found create
    :param path:
    :return: None
    """
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def get_time_now(raw: bool = False) -> str or datetime:
    """
    returns the tim at the call
    :param raw: if raw return datetime object else formatted string
    :return:
    """
    now = datetime.now()  # get current date and time
    time = now.strftime("%m/%d/%Y, %H:%M:%S")
    if not raw:
        return time
    else:
        return now


def get_time_sys() -> str:
    """
    returns as system writable time string
    :return:
    """
    now = datetime.now()  # get current date and time
    return now.strftime("%d-%m-%Y_%H-%M-%S")


def console_log(content: str, color, log_level: int) -> None:
    """
    prints a message in a given color, logg the message and resets Fore
    :param content: the message content
    :param color: the colour (Fore.)
    :param log_level: the log level (logging.)
    :return: None
    """
    if log_level == logging.CRITICAL or log_level == logging.FATAL or log_level == logging.ERROR:
        color = Fore.RED
        content = "CRASHED: " + content
    for c in content.split("\n"):
        logging.log(log_level, c)
        print(color + c + Fore.RESET)


def get_external_version(app: str, server: str = "https://github.com/Lainupcomputer/pycord-bb/blob/main/VERSIONS") -> list:
    """

    :param app:
    :param server:
    :return:
    """
    from urllib import request
    req = request.urlopen(server)
    data = req.read().decode('UTF-8')
    s = data.find(app + '_version==')
    return data[s:s + 20].split("==")


def check_version(app: str, version: str) -> str:
    """

    :param app:
    :param version:
    :return:
    """
    data = get_external_version(app)
    d_ver_s = data[1].split(".")
    v_ver_s = version.split(".")
    success = True
    success_l = False
    success_msg = ""
    names = {0: "Main", 1: "Secondary", 2: "Patch", 3: "Fix"}
    for i in range(len(d_ver_s)):
        if d_ver_s[i] != v_ver_s[i]:
            diff = abs(int(d_ver_s[i]) - int(v_ver_s[i]))
            if diff > 2:
                sys.exit()
            else:
                success_msg += f"({app}) {names[i]}: remote:{d_ver_s[i]} current:{v_ver_s[i]}, Update recommended.\n"
                success = False
                success_l = True
                break
    if success:
        success_msg += f"({app}) up to date. ({version})"
    else:
        if not success_l:
            success_msg += f"({app}) needs update to run properly. current: ({version}), remote: ({d_ver_s})"
    return success_msg
