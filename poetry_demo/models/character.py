from __future__ import annotations

from poetry_demo.models.health_bar import HealthBar
from poetry_demo.models.weapon import Weapon, WeaponType


class Character:
    def __init__(self, name: str, health: int = None) -> None:
        self.name = name
        self.health = health if health else 100
        self.health_max = self.health
        self.is_alive = True
        self.cure = 2

        self.weapon = Weapon(name="Na mão", weapon_type=WeaponType.Level_1)

    def use_cure(self):
        if self.cure:
            self.cure -= 1
            self.health += 15
            self.health = min(self.health, 100)

    def damage(self):
        return self.weapon.damage()

    def receive_damage(self, damage):
        self.health -= damage
        self.health = max(self.health, 0)
