from tacalepau.models import Weapon, WeaponType


def test_weapon_level_1_damage_should_be_between_2_and_3():
    weapon = Weapon("Na mão", WeaponType.Level_1)

    damage = weapon.damage()

    assert damage >= 2
    assert damage <= 3


def test_weapon_level_2_damage_should_be_between_5_and_6():
    weapon = Weapon("faca", WeaponType.Level_2)

    damage = weapon.damage()

    assert damage >= 5
    assert damage <= 6


def test_weapon_level_3_damage_should_be_between_7_and_8():
    weapon = Weapon("facão", WeaponType.Level_3)

    damage = weapon.damage()

    assert damage >= 7
    assert damage <= 8


def test_weapon_level_4_damage_should_be_between_9_and_10():
    weapon = Weapon("machado", WeaponType.Level_4)

    damage = weapon.damage()

    assert damage >= 9
    assert damage <= 10
