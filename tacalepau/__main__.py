from games import select_game, GameMode


def main(mode: GameMode):
    select_game(mode)


if __name__ == "__main__":
    main(GameMode.SURVIVAL)
