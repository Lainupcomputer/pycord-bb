import json
from pathlib import Path


class StorageContainer:
    def __init__(self, name: str, path: str = "storage", debug: bool = False):
        self.name = name
        self.data: dict = {}

        base = Path(path).absolute()
        base.mkdir(parents=True, exist_ok=True)
        self.path: Path = base / f"{self.name}.sc"

        if debug:
            print(Path(path).absolute().joinpath(f"{self.name}.sc"))

    def get(self, on_create=None) -> dict:
        if on_create is None:
            on_create = {}
        try:
            with open(self.path, "r") as f:
                self.data = json.load(f)
            return self.data

        except FileNotFoundError:
            with open(self.path, "w") as f:
                json.dump(on_create, f, indent=2)
            return on_create

        except json.JSONDecodeError:
            self.data = on_create
            with open(self.path, "w") as f:
                json.dump(on_create, f, indent=2)
            return self.data

    def set(self, data: dict = None) -> None:
        if data is None:
            data = self.data
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)
