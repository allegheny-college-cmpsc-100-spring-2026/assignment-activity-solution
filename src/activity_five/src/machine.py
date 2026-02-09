import time
import random
from typing import Any

class Pin:

    IN = 0
    OUT = 1
    PULL_UP = 1

    def __init__(self, id: Any, mode: Any, *args, **kwargs):
        self.id = id
        self.mode = mode
        self.val = 0
        if "value" in kwargs:
            self.press_type = kwargs["value"]
        else:
            self.press_type = [
                "short", "short", "short", "long",
                "short", "long",
                "short", "long",
                "short", "short", "long",
                "short", "long",
                "short", "short", "short", "short", "long"
            ]
        self.press_start = time.time()

    def value(self) -> int:
        press_duration = time.time() - self.press_start
        if len(self.press_type) == 0: return 1
        type = self.press_type[0]
        if type == "long" and press_duration > .5:
            self.press_type.pop(0)
            self.press_start = time.time()
            return 1
        if type == "short" and press_duration > .1:
            self.press_type.pop(0)
            self.press_start = time.time()
            return 1
        return 0

    def on(self):
        pass

    def off(self):
        pass