from classes.weapon import Sword, Bow
from classes.character import Fighter, Monster

def main():
    fighter = Fighter("Герой")
    monster = Monster("Злобный монстр")

    sword = Sword()
    bow = Bow()

    while True:
        choice = input("\nВыберите оружие (меч/лук): ")

        if choice == 'меч':
            fighter.change_weapon(sword)
        elif choice == 'лук':
            fighter.change_weapon(bow)
        else:
            print("Неверный выбор оружия!")
            continue

        print(f"\n{fighter.name} выбрал {choice}.")
        fighter.attack_with_current_weapon(monster)

        if not monster.is_alive():
            print(f"{monster.name} побеждён!")
            break

        # Монстр отвечает ударом
        if monster.is_alive():
            damage = monster.attack()
            fighter.take_damage(damage)

if __name__ == "__main__":
    main()