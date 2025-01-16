import random

class Fighter():
    def __init__(self, name, weapon = None):
        self.name = name
        self.health = 100
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