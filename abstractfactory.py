from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "Product A1"

class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "Product B1"

class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "Product A2"

class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "Product B2"

factory = ConcreteFactory1()
product_a = factory.create_product_a()
product_b = factory.create_product_b()

print(product_a.operation_a())  # "Product A1"
print(product_b.operation_b())  # "Product B1"