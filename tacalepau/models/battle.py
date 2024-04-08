from typing import Optional
from enum import Enum

from .player import Player
from .enemy import Enemy
from .character import Character


class Commands(str, Enum):
    ATTACK = "a",
    CURE = "c",
    COUNTER_ATTACK = "ca"


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
