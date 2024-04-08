from tacalepau.models import Battle, Player, Enemy, Commands


def test_instantiation():
    player = Player("Folha Seca")
    enemy = Enemy("Volante")

    battle = Battle(player, enemy)

    assert battle.winner is None


def test_player_turn__should_handle_player_attack():
    player = Player("Folha Seca")
    enemy = Enemy("Volante")
    battle = Battle(player, enemy)

    assert enemy.health == 100

    battle.player_turn(Commands.ATTACK)

    assert enemy.health < 100


def test_player_turn__should_handle_player_counter_attack():
    player = Player("Folha Seca")
    enemy = Enemy("Volante")
    battle = Battle(player, enemy)

    battle.player_turn(Commands.COUNTER_ATTACK)

    assert battle.enemy.health < 100 or battle.player.health < 100


def test_player_turn__should_handle_player_cure():
    player = Player("Folha Seca")
    enemy = Enemy("Volante")
    battle = Battle(player, enemy)

    battle.enemy_turn()

    assert player.health < 100

    battle.player_turn(Commands.CURE)

    assert player.health == 100


def test_enemy_turn_should_handle_player_attack():
    player = Player("Folha Seca")
    enemy = Enemy("Volante")
    battle = Battle(player, enemy)

    assert player.health == 100

    battle.enemy_turn()

    assert player.health < 100
