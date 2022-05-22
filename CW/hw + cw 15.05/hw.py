class Cat:
    def __init__(self, name: str):
        self.name = name

    def say_meow(self):
        print(f"Кошка {self.name} помяукала!")

    def scratch(self):
        print(f"Кошка {self.name} поцарапала диван!")

class Sofa:
    def __init__(self, scratch: int):
        self.scratch = scratch

    def get_hit(self):
        self.scratch += 1

    def check_hit(self):
        if self.scratch == 3:
            print('Диван разодран!')
            return True
        else:
            print('Еще пару таких фокусов, и он развалится!')

malinka = Cat("Малинка") #  Имя кошки 
sofa = Sofa(0) # Прочность дивана в у.е


for tries in range(5):
    malinka.say_meow()
    malinka.scratch()
    
    sofa.get_hit()
    
    if sofa.check_hit(): 
        break
