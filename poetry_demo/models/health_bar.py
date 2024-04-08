import os

os.system("")


class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {"red": "\033[91m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "green": "\033[92m",
                    "green2": "\033[32m",
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "default": "\033[0m"}

    def __init__(self, character, length: int = None, is_colored: bool = True, color: str = None) -> None:
        self.character = character
        self.length = length if length else 100
        self.max_value = character.health_max
        self.current_value = character.health
        self.is_colored = is_colored
        self.color = color if color else self.colors["default"]
        self.__update_remaining_bars()
        self.__update_lost_bars()

    def render(self):
        print(f"{self.character.name}: {self.character.health}/{self.character.health_max}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{self.remaining_bars * self.symbol_remaining}"
              f"{self.lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}\n")

    def update(self) -> None:
        self.current_value = self.character.health
        self.__update_remaining_bars()
        self.__update_lost_bars()

    def __update_remaining_bars(self):
        self.remaining_bars = round(self.current_value / self.max_value * self.length)

    def __update_lost_bars(self):
        self.lost_bars = self.length - self.remaining_bars
