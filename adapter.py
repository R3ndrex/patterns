# Інтерфейс тварини
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class CatAdapter(Animal):
    def __init__(self, cat):
        self.cat = cat

    def speak(self):
        return self.cat.meow()

class Cat:
    def meow(self):
        return "Meow!"


dog = Dog()
print(dog.speak())  #  Woof!

cat = Cat()
cat_adapter = CatAdapter(cat)
print(cat_adapter.speak())  #  Meow!