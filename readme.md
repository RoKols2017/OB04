# Боец против Монстра

Этот проект представляет консольную игру, где игрок управляет бойцом, сражающимся с монстром. Игрок выбирает оружие для атаки, а монстр отвечает случайным образом. Цель игры — победить монстра, сохранив жизнь бойца.

## Особенности
- Выбор оружия: меч или лук.
- Реалистичная система атаки с разным уроном для каждого типа оружия.
- Монстр наносит случайный урон при атаке.
- Проверка состояния здоровья бойца и монстра для определения победы.

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone <ссылка на репозиторий>
   cd <папка_репозитория>
    ```
2. Убедитесь, что у вас установлен Python 3.8+.

3. (Опционально) Создайте виртуальное окружение:

   ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/MacOS
    venv\Scripts\activate     # Для Windows
   ```
4. Установите зависимости (если они есть):

    ```
    pip install -r requirements.txt
    ```
## Структура проекта
    
    .
    ├── classes/
    │   ├── weapon.py        # Реализация классов оружия (меч, лук)
    │   ├── character.py     # Реализация классов персонажей (боец, монстр)
    ├── main.py              # Основной игровой сценарий
    ├── README.md            # Документация проекта
    
## Использование
1. Запустите игру:

    ```
    python main.py
    ```
2. Следуйте инструкциям в консоли:

- Выберите оружие: меч или лук.
- Атакуйте монстра и следите за состоянием здоровья персонажей.
3. Игра продолжается, пока боец или монстр не погибнут.

## Пример игры

    Выберите оружие (меч/лук): меч

    Герой выбрал меч.
    Боец наносит удар мечом.
    Злобный монстр получил урон. Осталось здоровья: 40

    Монстр кусает бойца.
    Герой получил урон. Осталось здоровья: 90

## Требования
Python 3.8+
Лицензия
Этот проект распространяется под MIT License.

## Контакты
Если у вас есть вопросы или предложения, напишите на RoKols2017@gmail.com.   