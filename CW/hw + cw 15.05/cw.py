# Класс
class Hero:
    # Метод-конструктор
    def __init__(self, name, attack): # константа
        self.name = name
        self.attack = attack
    # Метод
    def your_name(self):
        print(f"Your name is {self.name}")
    
    def attack_enemy(self):
        print(f"Бум! Ты ударил врага и нанес ему {self.attack} урона")
        
class Enemy:
    def __init__(self, attack, hp):
        self.attack = attack
        self.hp = hp
    
    def get_hit(self, attack_hero, name_hero):
        print(f"Враг получил удар от {name_hero}")
        print(f"Здоровья до удара: {self.hp}")
        self.hp -= attack_hero
        print(f"Здоровье после удара: {self.hp}")

# Экземпляр
adam = Hero('Адам', 20)
eva = Hero("Ева", 10)

orc = Enemy(5, 100)

orc.get_hit(adam.attack, adam.name) 
orc.get_hit(eva.attack, eva.name)

# Паттерны - приемы, которые применяются для повышения эффективности кода
