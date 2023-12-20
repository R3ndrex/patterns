from abc import ABC, abstractmethod

class AnimalImplementation(ABC):
    @abstractmethod
    def speak_implementation(self) -> str:
        pass

class DogImplementation(AnimalImplementation):
    def speak_implementation(self) -> str:
        return "Гав!"


class CatImplementation(AnimalImplementation):
    def speak_implementation(self) -> str:
        return "Мяу!"


class FishImplementation(AnimalImplementation):
    def speak_implementation(self) -> str:
        return "Бульк!"
    
class AnimalAbstraction(ABC):
    def __init__(self, implementation: AnimalImplementation) -> None:
        self.implementation = implementation

    def speak(self) -> str:
        return (f"AnimalAbstraction: Base speak with:\n"
                f"{self.implementation.speak_implementation()}")


class AnimalExtendedAbstraction(AnimalAbstraction):
    def speak(self) -> str:
        return (f"AnimalExtendedAbstraction: Extended speak with:\n"
                f"{self.implementation.speak_implementation()}")

def client_code(abstraction: AnimalAbstraction) -> None:
    print(abstraction.speak())


if __name__ == "__main__":
    dog_implementation = DogImplementation()
    abstraction = AnimalAbstraction(dog_implementation)
    client_code(abstraction)

    cat_implementation=CatImplementation()
    extended_abstraction = AnimalExtendedAbstraction(cat_implementation)
    client_code(extended_abstraction)

    fish_implementation = FishImplementation()
    abstraction = AnimalAbstraction(fish_implementation)
    client_code(abstraction)