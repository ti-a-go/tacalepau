from enum import Enum

from tacalepau.models import SurvivalMode


class GameMode(Enum):
    SURVIVAL = 1,
    CHAMPIONSHIP = 2,
    STORY = 3


def select_game(mode: GameMode):
    match mode:
        case mode.SURVIVAL:
            game = SurvivalMode()
            game.play()
        case mode.CHAMPIONSHIP:
            championship_mode()
        case mode.STORY:
            story_mode()


def championship_mode():
    # battle to win the trophy
    pass


def story_mode():
    # battle to save the day
    pass
