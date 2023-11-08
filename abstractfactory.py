from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

def get_animal_speech(factory):
    animal = factory.create_animal()
    return animal.speak()

dog_factory = DogFactory()
cat_factory = CatFactory()

dog_speech = get_animal_speech(dog_factory)
print("Dog:", dog_speech)  # Woof!

cat_speech = get_animal_speech(cat_factory)
print("Cat:", cat_speech)  # Meow!