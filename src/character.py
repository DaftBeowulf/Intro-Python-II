import random


class Character():
    def __init__(self):
        self.health = 100
        self.power = 20
        self.defense = 10

    def attack(self, enemy):
        dmg = int(round(self.power*(1+random.random())))-enemy.defense
        enemy.health -= dmg
        print(
            f'\n{self.name} deals {dmg} points of damage to {enemy.name}!\n{enemy.name} is at {enemy.health} hp.')
        if enemy.health <= 0:
            print(
                f'\n{enemy.name} has been slain and {self.name} is victorious!')
