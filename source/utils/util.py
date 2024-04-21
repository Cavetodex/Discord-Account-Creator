from typing import Union, Any
import json


class Utilities:
    @staticmethod
    def config(path: str) -> Union[Any]:
        with open(path, "r") as f:
            return json.load(f)

    @staticmethod
    def readfile(direct: str, level: int) -> list[Any]:
        path = ("./" * level) + direct
        with open(path, "r") as f:
            return f.read().splitlines()
