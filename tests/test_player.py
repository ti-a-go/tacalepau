from poetry_demo.models.player import Player


def test_counter_attack__should_return_a_damage():
    player = Player("Foia Seca")

    damage = player.counter_attack(10)

    assert isinstance(damage, int)
    if damage == 0:
        assert player.health == 80

    if damage > 0:
        assert player.health == 100
