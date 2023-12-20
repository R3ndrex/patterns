class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} говорить"


class Dog(Animal):
    def speak(self):
        return "Гав!"


class Cat(Animal):
    def speak(self):
        return "Мяу!"


class Fish(Animal):
    def speak(self):
        return "Бульк!"
    
class AnimalManager:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def get_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal
        return None


manager = AnimalManager()

manager.add_animal(Dog("Рекс"))
manager.add_animal(Cat("Мурка"))
manager.add_animal(Fish("Золота рибка"))

for animal in manager.animals:
    print(animal.speak())