from random import uniform

from .character import Character


class Player(Character):

    def __init__(self, name: str, health: int = None):
        super().__init__(name=name, health=health)

    def counter_attack(self, enemy_damage):
        damage = self.damage() * 2 \
                if self.__counter_attack_success() else 0
        if not damage:
            self.receive_damage(enemy_damage * 2)
        return damage

    @staticmethod
    def __counter_attack_success():
        return uniform(0, 1) < 0.6
