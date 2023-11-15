import copy

class AnimalPrototype:
    def clone(self):
        pass

class Dog(AnimalPrototype):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def clone(self):
        return copy.deepcopy(self)

class Cat(AnimalPrototype):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def clone(self):
        return copy.deepcopy(self)


dog_prototype = Dog("Боня", "Англійський бульдог")
cat_prototype = Cat("Персик", "Білий")

dog_clone1 = dog_prototype.clone()
dog_clone2 = dog_prototype.clone()

cat_clone1 = cat_prototype.clone()
cat_clone2 = cat_prototype.clone()

print(f"Dog 1: {dog_clone1.name}, {dog_clone1.breed}") # Боня, Англійський бульдог
print(f"Dog 2: {dog_clone2.name}, {dog_clone2.breed}") # Боня, Англійський бульдог

print(f"Cat 1: {cat_clone1.name}, {cat_clone1.color}") # Персик, Білий
print(f"Cat 2: {cat_clone2.name}, {cat_clone2.color}") # Персик, Білий