class AnimalSingleton:
    _instance = None
    def __new__(cls, name, tail_length, color):
        if not cls._instance:
            cls._instance = super(AnimalSingleton, cls).__new__(cls)
            cls._instance.name = name
            cls._instance.tail_length = tail_length
            cls._instance.color = color
        return cls._instance

singleton_animal = AnimalSingleton(name="Cat", tail_length=12, color="Gray")
print("Name:", singleton_animal.name)
print("Tail Length:", singleton_animal.tail_length)
print("Color:", singleton_animal.color)

new_animal = AnimalSingleton(name="Dog", tail_length=8, color="Brown")
print("Name:", new_animal.name)  # Cat
print("Tail Length:", new_animal.tail_length)  # 12
print("Color:", new_animal.color)  # Gray

print(singleton_animal is new_animal)  # True