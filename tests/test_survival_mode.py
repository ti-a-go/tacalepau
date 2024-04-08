from tacalepau.models import SurvivalMode


def test_instantiation():
    game = SurvivalMode()

    assert isinstance(game, SurvivalMode)