class Person:
    # __slots__ - это магический метод, который ограничивает кол-во принимаемых классом объектов
    #__slots__ = ['name', 'age', 'info']
    status = 'OK'
    def __init__(self, name, age, info = 'sss'):
        self.name = name
        self.age = age
        self.info = info
    
    def test():
        pass

# __dict__ - это магический метол, который выводит информацию о свойствах объекта
# self - это сущность, которая связывает экземпляр и класс (ссылка на экземпляр класса)
person = Person('aa', 4)

print(person.__dict__)

person.info = 'ssss1'
print(person.__dict__)