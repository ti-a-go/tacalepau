from typing import Optional

from poetry_demo.models.player import Player
from poetry_demo.models.enemy import Enemy
from poetry_demo.models.character import Character
from poetry_demo.commands import Commands


class Battle:

    def __init__(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.winner: Optional[Character] = None
        self.result = None

    def player_turn(self, command: Commands):
        match command:
            case command.ATTACK:
                self.enemy.receive_damage(
                    self.player.damage()
                )
            case command.COUNTER_ATTACK:
                self.enemy.receive_damage(
                    self.player.counter_attack(self.enemy.weapon.damage())
                )
            case command.CURE:
                self.player.use_cure()
        self.__update_winner()

    def enemy_turn(self):
        self.player.receive_damage(
            self.enemy.damage()
        )
        self.__update_winner()

    def __update_winner(self):
        if self.player.health < 1:
            self.winner = self.enemy
        if self.enemy.health < 1:
            self.winner = self.player
