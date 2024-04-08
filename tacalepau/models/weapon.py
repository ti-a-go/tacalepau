from random import randint
from enum import Enum


class WeaponType(Enum):
    Level_1 = 1
    Level_2 = 2
    Level_3 = 3
    Level_4 = 4


class Weapon:
    def __init__(self,
                 name: str,
                 weapon_type: WeaponType,
                 ) -> None:
        self.name = name
        self.weapon_type = weapon_type

    def damage(self):
        if self.weapon_type == WeaponType.Level_1:
            return randint(2, 3)
        if self.weapon_type == WeaponType.Level_2:
            return randint(5, 6)
        if self.weapon_type == WeaponType.Level_3:
            return randint(7, 8)
        if self.weapon_type == WeaponType.Level_4:
            return randint(9, 10)

