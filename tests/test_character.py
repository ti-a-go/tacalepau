from random import randint

from poetry_demo.models import Character, Weapon


name = "Foia Seca"


def test_instantiation():
    character = Character(name)

    assert character.name == name
    assert character.health == 100
    assert character.health_max == 100
    assert isinstance(character.weapon, Weapon)
    assert character.weapon.name == "Na mão"


def test_damage__should_return_an_integer_positive():
    character = Character(name)

    damage = character.damage()

    assert isinstance(damage, int)
    assert damage >= 0


def test_receive_damaged__should_decrease_health_according_to_the_damage_received():
    character = Character(name)
    damage = randint(1, 100)
    expected_health = character.health - damage

    character.receive_damage(damage)

    assert character.health == expected_health


def test_use_cure__should_restore_health_in_twenty_five():
    # Arrange
    character = Character(name)
    damage = 10
    expected_health = character.health - damage * 3

    # Act
    character.receive_damage(damage)
    character.receive_damage(damage)
    character.receive_damage(damage)

    # Assert
    assert character.health == expected_health

    # Arrange
    expected_health = character.health + 15

    # Act
    character.use_cure()

    # Assert
    assert character.health == expected_health
