from random import randint

class Hero:
    def __init__(self, name, dmg, hp, energy):
        self.name = name
        self.dmg = dmg
        self.hp = hp
        self.energy = energy
    
    def attack(self, enemy_hp):
        enemy_hp -= self.dmg
        return enemy_hp

    def defend(self):
        self.energy -= 10

    def evade(self):
        self.energy -= 15

    def overdose(self):
        if self.energy <= 0:
            self.hp -= 10

good_hero = Hero('Привид Києва', 20, 100, 100)
bad_hero = Hero('Орк', 20, 100, 100)

while good_hero.hp > 0 and bad_hero.hp > 0:
    if randint(1, 2) == 1:
        if randint(1, 3) == 1:
            if bad_hero.energy < 0:
                bad_hero.overdose()

            print(f"{bad_hero.name} Защищается!")
            bad_hero.defend()

        elif randint(1, 3) == 2:
            if bad_hero.energy < 0:
                bad_hero.overdose()

            print(f"{bad_hero.name} Уклоняется!")
            bad_hero.evade()

        else:
            print(f"{bad_hero.name} Получает урон!")
            bad_hero.hp = good_hero.attack(bad_hero.hp)
    
    elif randint(1, 2) == 2:
        if randint(1, 3) == 1:
            if good_hero.energy < 0:
                good_hero.overdose()

            print(f"{good_hero.name} Защищается!")
            good_hero.defend()

        elif randint(1, 3) == 2:
            if good_hero.energy < 0:
                good_hero.overdose()

            print(f"{good_hero.name} Уклоняется!")
            good_hero.evade()
        else:
            print(f"{good_hero.name} Получает урон!")
            good_hero.hp = bad_hero.attack(good_hero.hp)
            

if good_hero.hp > bad_hero.hp:
    print(f"{good_hero.name} Победил!")
    print(good_hero.hp, bad_hero.hp)


else:
    print(f"{bad_hero.name} Победил!")
    print(good_hero.hp, bad_hero.hp)