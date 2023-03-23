import os


def check_create_dir(path: str):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass