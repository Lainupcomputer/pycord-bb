"""
Ez Storage Module

Copyright (C) 2023 LainUpComputerSolution. All Rights Reserved.

To use, 'import ez_storage' and save time typing!
"""
import json
import logging
from .classes import Ez_Dict, Ez_Data, Storage_Path_Error
from .utils import check_create_dir, get_time_sys, console_log
from colorama import Fore, Back

_VERSION = "1.4.0.0"


class Storage:
    """
    Base class for the Ez Storage system. This class handles everything necessary for storing and retrieving items from the filesystem.

    :param: kwargs: Keyword arguments that specify the path to the file, the directory path, and the prefix for the storage instance.
        path (str): Path to the file.
        dir (str): Directory path.
        prefix (str): Prefix for the storage instance.

    :raises: Storage_Path_Error: If the 'path' argument is not specified.

    :return: None

    Side Effects:
    - Sets the '_cached' attribute of the storage object to None.
    - Sets the '_path' attribute of the storage object to the 'path' argument.
    - Sets the '_dir' attribute of the storage object to the 'dir' argument or './' if not specified.
    - Sets the '_prefix' attribute of the storage object to the 'prefix' argument or 'Ez_Storage' if not specified.
    - Initializes the '_default_json' attribute of the storage object with a dictionary containing the file header.
    - Calls the '_load' method to load the content of the JSON file into the '_cached' attribute of the storage object.

    Methods:
    - __repr__(self) -> str:
        Returns a printable representation of the `Storage` object for debugging and development purposes.

    - cached(self) -> classes.Ez_Dict:
        Gets the cached Ez_Dict.

    - _load(self) -> None:
        Reads a JSON file and converts its content into an Ez_Dict object. If the file is not found, it creates a new one with the default JSON content. If the file is invalid, it creates a backup, replaces the file with the default JSON content, and logs a warning message.

    - _write_file_json(self, data: dict) -> None:
        Writes a dictionary to a file at the specified path in JSON format.

    """
    def __init__(self, **kwargs) -> None:
        """
            Initializes an instance of the Ez Storage Base Class.
            This class holds all the necessary information for accessing and maintaining subclasses.
            It handles everything necessary for storing and retrieving items from the filesystem.
            :param: kwargs: Keyword arguments that specify the path to the file, the directory path, and the prefix for the storage instance.
                path (str): Path to the file.
                dir (str): Directory path.
                prefix (str): Prefix for the storage instance.

            :raises: Storage_Path_Error: If the 'path' argument is not specified.

            :return: None

            Side Effects:
            - Sets the '_cached' attribute of the storage object to None.
            - Sets the '_path' attribute of the storage object to the 'path' argument.
            - Sets the '_dir' attribute of the storage object to the 'dir' argument or './' if not specified.
            - Sets the '_prefix' attribute of the storage object to the 'prefix' argument or 'Ez_Storage' if not specified.
            - Initializes the '_default_json' attribute of the storage object with a dictionary containing the file header.
            - Calls the '_load' method to load the content of the JSON file into the '_cached' attribute of the storage object.
            """
        self._cached = None
        # get file path
        self._path: str = kwargs.get("path")
        if not self._path:
            raise Storage_Path_Error
        # get subdirectory
        self._dir: str = kwargs.get("dir")
        if not self._dir:
            self._dir = str("./")
        # get prefix
        self._prefix = kwargs.get("prefix")
        if not self._prefix:
            self._prefix = str("Ez_Storage")
        # default file header
        self._default_json = dict({"ez-storage": {"version": str(_VERSION), "opened": get_time_sys(True)}})
        # initial load
        self._load()

    def __repr__(self) -> str:
        """
        Returns a printable representation of the `Ez_Storage` object for debugging and development purposes.
        :return: A string with basic information about the `Ez_Storage` object, including its version and location.
        """
        return (f"{Fore.BLUE}{Back.GREEN}version: {_VERSION}{Back.RESET}\n"
                f"{Back.GREEN}location: {self._dir}{self._path}{Back.RESET}{Fore.RESET}")

    @property
    def cached(self) -> classes.Ez_Dict:
        """
        Gets the cached Ez_Dict
        :return: An instance of `classes.Ez_Dict` containing the cached Ez_Dict.
        """
        return self._cached

    def _load(self) -> None:
        """
        Reads a JSON file and converts its content into an Ez_Dict object.
        If the file is not found, it creates a new one with the default JSON content.
        If the file is invalid, it creates a backup, replaces the file with the default JSON content, and logs a warning message.

        :return: None

        Raises:
        - FileNotFoundError: If the JSON file is not found and cannot be created.
        - json.decoder.JSONDecodeError: If the JSON file is invalid and cannot be replaced.

        Side Effects:
        - Creates a JSON file with the default content if it doesn't exist.
        - Replaces an invalid JSON file with the default content.
        - Logs warning messages if the file is not found or invalid.
        - Sets the '_cached' attribute of the storage object to an Ez_Dict instance containing the parsed content of the JSON file.
        """
        check_create_dir(self._dir)
        try:
            f = open(self._dir + self._path)
            json.load(f)
            f.close()

        except FileNotFoundError:
            self._write_file_json(self._default_json)
            console_log(f"[{self._prefix}]:storage_file: not found -> rebase", Fore.YELLOW, logging.WARNING)

        except json.decoder.JSONDecodeError:
            console_log(f"[{self._prefix}]:storage_file: invalid -> backup & rebase", Fore.YELLOW, logging.WARNING)
            self._write_file_json(self._default_json)

        finally:
            # return Ez_Dict
            with open(self._dir + self._path, "r") as f:
                self._cached = Ez_Dict(self, data=json.load(f))

    def _write_file_json(self, data: dict) -> None:
        """
        write a dict to file at path in json format
        :param data: dict to write to file
        :return: None
        """
        with open(self._dir + self._path, "w") as f:
            json.dump(data, f, indent=2)

    def get(self, entity: str, **kwargs):
        return self._cached.get(entity, **kwargs)

    def add(self, entity: str, value: (int, str, dict, tuple, list), **kwargs):
        return self._cached.add(entity, value, **kwargs)

    def update(self, entity: str, value: (int, str, dict, tuple), **kwargs):
        return self._cached.add(entity, value, overwrite=True, **kwargs)
