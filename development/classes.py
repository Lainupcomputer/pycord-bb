from .utils import get_time_sys


class Storage_Path_Error(Exception):
    """
    Exception class for when no storage path is provided.

    Methods:
        __str__(self):
            Returns a string representation of the error message.

    Example Output:
        Storage Error: no path provided.
        provide a path as keyword Argument: path='your_path'
    """

    def __str__(self):
        """
        Returns a string representation of the error message.
        """
        return "Storage Error: no path provided. \n provide a path as keyword Argument: path='your_path'"


class Storage_Compatibility_Error(Exception):
    """
    Exception class for when the provided storage file is incompatible.

    Methods:
        __str__(self):
            Returns a string representation of the error message.

    Example Output:
        Storage Error: the provided Storage File is incompatible.
        check your file at: directory and path declared on initialisation of Storage
    """

    def __str__(self):
        """
        Returns a string representation of the error message.
        """
        return "Storage Error: the provided Storage File is incompatible.\n" \
               "check your file at: directory and path declared on initialisation of Storage"


class Storage_Item_Error(Exception):
    """
    Exception raised when an item cannot be found in storage system.

    Methods:
        __str__(): Returns a string representation of the exception.

    Example Output:
        Storage Error: the item you are looking for could not be found.
        check your typing
    """

    def __str__(self):
        """
        Returns a string representation of the exception.
        """
        return "Storage Error: the item you are looking for could not be found.\n" \
               "check your typing"


class Ez_Data:
    def __init__(self, storage, **kwargs) -> None:
        self._storage = storage
        self._version = "1.4.0.0"
        self._type = "undefined"
        self._data = None
        self._file_header = None

    def __repr__(self) -> str:
        return f"EzData:type={self._type}:path={self._storage._path}\n" \
               f""

    @property
    def data(self):
        return self._data

    def _get_header(self, method: str):
        if method == "json":
            self._file_header = self.data.get("ez-storage")

    def _set_header(self, method: str):
        if method == "json":
            self.data["ez-storage"]["opened"] = get_time_sys(True)
            self._storage._write_file_json(self.data)

    def _check_compatibility(self) -> bool:
        if not self._file_header.get('version') == self._version:
            return False
        return True

    def _check_reload(self) -> bool:
        print(int(self._file_header.get('opened')) - int(get_time_sys(True)))
        if self.data is None:
            self._set_header("json")
            self._storage._load()
            return True
        if int(self._file_header.get('opened')) - int(get_time_sys(True)) < 10:
            self._set_header("json")
            self._storage._load()
            return True
        return True

    def get(self, *args, **kwargs):
        ...

    def add(self, *args, **kwargs):
        ...

    def rem(self, *args, **kwargs):
        ...


class Ez_Dict(Ez_Data):
    def __init__(self, storage, **kwargs):
        super().__init__(storage, **kwargs)
        self._type = "Ez_Dict"
        self._data: dict = kwargs.get("data")
        self._get_header(method="json")

    def get(self, entity: str, **kwargs):
        res = None
        if not self._check_compatibility():
            raise Storage_Compatibility_Error
        self._check_reload()
        within = kwargs.get("within")
        if within:
            if isinstance(within, str):
                base = self.data.get(within)
                res = base.get(entity)

            elif isinstance(within, list):
                base = self.data.get(within[0])
                within.pop(0)
                for s in within:
                    base = base.get(s)
                res = base.get(entity)
        else:
            res = self.data.get(entity)
        if res is None:
            raise Storage_Item_Error
        else:
            return res

    def add(self, entity: str, value: (int, str, dict, tuple), **kwargs):
        if not self._check_compatibility():
            raise Storage_Compatibility_Error

        self._check_reload()

        if not self.get(entity):
            self.data[entity] = value
            self._storage._write_file_json(self.data)
            return True

        if kwargs.get("overwrite"):
            self.data[entity] = value
            self._storage._write_file_json(self.data)
            return True

        if kwargs.get("debug"):
            print(f"entity:{entity} was not added, existing and overwrite is toggled off")

        return False

