class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class AnimalTranslator(Animal):
    def __init__(self, animal):
        self.animal = animal

    def speak(self):
        return self.animal.speak()

dog = Dog()
cat = Cat()

translator = AnimalTranslator(dog)
translator.speak() # Woof!

translator = AnimalTranslator(cat)
translator.speak() # Meow!