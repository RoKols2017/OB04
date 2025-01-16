from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self, target):
        pass


class Sword(Weapon):
    def attack(self, target):
        print("Боец наносит удар мечом.")
        return 10 # Урон от меча


class Bow(Weapon):
    def attack(self, target):
        print("Боец стреляет из лука.")
        return 7 # Урон от лука