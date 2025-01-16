from abc import ABC, abstractmethod
import random

class Character(ABC):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    @abstractmethod
    def take_damage(self, damage):
        pass

    @abstractmethod
    def is_alive(self):
        pass


class Fighter(Character):
    def __init__(self, name, weapon = None):
        super().__init__(name)
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} погиб!")
        else:
            print(f"{self.name} получил урон. Осталось здоровья: {self.health}")

    def is_alive(self):
        return self.health > 0

    def attack_with_current_weapon(self, target):
        if self.weapon:
            damage = self.weapon.attack(target)
            target.take_damage(damage)
        else:
            print("У бойца нет оружия!")


class Monster(Character):
    def __init__(self, name, health=50):
        super().__init__(name, health)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} побеждён!")
        else:
            print(f"{self.name} получил урон. Осталось здоровья: {self.health}")

    def is_alive(self):
        return self.health > 0

    def attack(self):
        damage = random.randint(5, 15)  # Монстр наносит случайный урон от 5 до 15
        print(f"Монстр кусает бойца.")
        return damage
