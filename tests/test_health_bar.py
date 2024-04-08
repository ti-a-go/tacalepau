from poetry_demo.models import Character, HealthBar


def test_health_bar_instantiation():
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
                    "default": "\033[0m"
                    }
    character = Character("Folha Seca")
    length = 100
    health_bar = HealthBar(character)

    assert health_bar.character is character
    assert health_bar.symbol_remaining == symbol_remaining
    assert health_bar.symbol_lost == symbol_lost
    assert health_bar.barrier == barrier
    assert health_bar.colors == colors
    assert health_bar.character is character
    assert health_bar.length == length
    assert health_bar.max_value == character.health_max
    assert health_bar.current_value == character.health
    assert health_bar.is_colored is True
    assert health_bar.color == colors["default"]
    assert health_bar.remaining_bars == length
    assert health_bar.lost_bars == 0
