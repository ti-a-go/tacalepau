from random import choice

from poetry_demo.models.weapon import Weapon, WeaponType


fists = Weapon(name="Na mão", weapon_type=WeaponType.Level_1)
knife = Weapon(name="Faca", weapon_type=WeaponType.Level_2)
machete = Weapon(name="Facão", weapon_type=WeaponType.Level_3)
axe = Weapon(name="Machado", weapon_type=WeaponType.Level_4)


def get_random_weapon():
    return choice([fists, knife, machete, axe])
