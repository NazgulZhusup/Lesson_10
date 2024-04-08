import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name}, нанося {self.attack_power} очков урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)
            turn += 1
            self.status()

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

    def status(self):
        print(f"Здоровье {self.player.name}: {self.player.health}")
        print(f"Здоровье {self.computer.name}: {self.computer.health}")
        print("-" * 20)

# Создаем героев
player = Hero("Игрок")
computer = Hero("Компьютер", attack_power=15)

# Начинаем игру
game = Game(player, computer)
game.start()

