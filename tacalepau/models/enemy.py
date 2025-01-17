from .character import Character
from .weapon import Weapon


class Enemy(Character):

    def __init__(self, name: str, health: int = None, weapon: Weapon = None):
        super().__init__(name=name, health=health)
        self.weapon = weapon if weapon else self.weapon
