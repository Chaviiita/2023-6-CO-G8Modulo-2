from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy2 import Enemy2

import random
class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy_list = {0: Enemy(), 1: Enemy2()}

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len (self.enemies)<1:
            self.enemies.append(self.enemy_list[random.randint(0,1)])