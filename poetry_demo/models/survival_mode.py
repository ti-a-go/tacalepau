import os

from poetry_demo.models.battle import Battle
from poetry_demo.models.player import Player
from poetry_demo.models.enemy import Enemy
from poetry_demo.models.health_bar import HealthBar
from poetry_demo.commands import Commands


class SurvivalMode:

    def __init__(self):
        self.__player_command = None
        self.__is_player_command_valid = False

        self.__player = Player("Foia Seca")
        self.__player_health_bar = HealthBar(self.__player, color=HealthBar.colors.get("green"))

        self.__enemy = Enemy("Volante")
        self.__enemy_health_bar = HealthBar(self.__enemy, color=HealthBar.colors.get("red"))

        self.__battle = Battle(self.__player, self.__enemy)

    def play(self):
        while True:
            self.__render()

            self.__battle.player_turn(
                self.__get_user_command()
            )
            self.__update_health_bar()
            self.__render()
            self.__is_player_command_valid = False
            if self.__battle.winner:
                break

            self.__battle.enemy_turn()
            self.__update_health_bar()
            self.__render()
            if self.__battle.winner:
                break

            self.__update_health_bar()
            self.__render()

        self.__render_result()

    def __get_user_command(self) -> Commands:
        while not self.__is_player_command_valid:
            command = input()
            if command in list(Commands):
                self.__player_command = Commands(command)
                self.__is_player_command_valid = True
        return self.__player_command

    def __render(self):
        os.system("clear")
        self.__render_commands_help()
        self.__render_player_status()
        self.__player_health_bar.render()
        self.__enemy_health_bar.render()

    def __update_health_bar(self):
        self.__player_health_bar.update()
        self.__enemy_health_bar.update()

    def __render_player_status(self):
        print(f"{self.__player.name}\n"
              f" saúde: {self.__player.health}\n"
              f" chás: {self.__player.cure}\n")

    @staticmethod
    def __render_commands_help():
        print(f"COMANDOS:\n"
              f"Digite um comando e aperte 'Enter'\n\n"
              f"a (atacar) = ataca o inimigo com a arma equipada.\n"
              f"c (chá) = recupera a vida.\n"
              f"ca (contra ataque) = tem 50% de chance do dano ser revertido para o inimigo, mas se falhar recebe muito mais dano.\n")

    def __render_result(self):
        print(f"{self.__battle.winner.name} Venceu!")
