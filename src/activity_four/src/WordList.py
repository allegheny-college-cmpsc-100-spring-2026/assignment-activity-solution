from pathlib import Path
from typing import Any, Iterator, Generator

class List:

    @staticmethod
    def load(path_to_data: str = __file__) -> Generator[str, None, None]:
        path = Path(path_to_data)
        with open(f"{path.parent.absolute()}/data/words.list", "r") as fh:
            return iter([word.strip() for word in fh.readlines()])