import random
from classes.fighter import Fighter


class Monster(Fighter):
    def __init__(self, name, health=50):
        super().__init__(name, None)
        self.health = health

    def attack(self):
        """Реализация метода атаки монстра"""
        damage = random.randint(5, 15)  # Монстр наносит случайный урон от 5 до 15
        print(f"Монстр кусает бойца.")
        return damage