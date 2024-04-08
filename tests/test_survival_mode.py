from poetry_demo.models.survival_mode import SurvivalMode


def test_instantiation():
    game = SurvivalMode()

    assert isinstance(game, SurvivalMode)