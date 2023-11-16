class Animal:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show(self):
        print("Animal parts:", ", ".join(self.parts))

class AnimalBuilder:
    def build_legs(self):
        pass

    def build_head(self):
        pass

    def get_result(self):
        pass

class DogBuilder(AnimalBuilder):
    def __init__(self):
        self.animal = Animal()

    def build_legs(self):
        self.animal.add_part("Dog legs")

    def build_head(self):
        self.animal.add_part("Dog head")
    def build_tail(self):
        self.animal.add_part("Dog tail")

    def get_result(self):
        return self.animal


class CatBuilder(AnimalBuilder):
    def __init__(self):
        self.animal = Animal()

    def build_legs(self):
        self.animal.add_part("Cat legs")

    def build_head(self):
        self.animal.add_part("Cat head")
    def build_tail(self):
        self.animal.add_part("Cat tail")

    def get_result(self):
        return self.animal


class ZooKeeper:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_legs()
        self.builder.build_head()
        self.builder.build_tail()

if __name__ == "__main__":

    dog_builder = DogBuilder()
    zoo_keeper1 = ZooKeeper(dog_builder)
    zoo_keeper1.construct()
    dog = dog_builder.get_result()
    dog.show()

    cat_builder = CatBuilder()
    zoo_keeper2 = ZooKeeper(cat_builder)
    zoo_keeper2.construct()
    cat = cat_builder.get_result()
    cat.show()