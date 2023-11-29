class CarShowroom:
    _instance = None
    cars = {}
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CarShowroom, cls).__new__(cls)
        return cls._instance

    def add_car(self,car_name, car_price):
        self.cars[car_name] = car_price

    def get_car_price(self, car_name):
        return self.cars.get(car_name)
    
    def get_available_cars(self):
        return list(self.cars)
    
    def buy_car(self, car_name, money):
        if car_name not in self.cars:
            raise ValueError("There is no car with this name")
        if self.cars[car_name] > money:
            raise ValueError("Not enough money to buy the car")
        change = money - self.cars[car_name]
        return change

carshowroom1 = CarShowroom()
carshowroom1.add_car("Buggatti", 5000)
available_cars = carshowroom1.get_available_cars()
for car in available_cars:
    price = carshowroom1.get_car_price(car)
    print(f"{car}: ${price}")

carshowroom = CarShowroom()
available_cars = carshowroom.get_available_cars()
for car in available_cars:
    price = carshowroom.get_car_price(car)
    print(f"{car}: ${price}")

carshowroom.add_car("Toyota", 4600)
available_cars = carshowroom.get_available_cars()
for car in available_cars:
    price = carshowroom.get_car_price(car)
    print(f"{car}: ${price}")

change = carshowroom.buy_car("Buggatti", 7000) 
print(f"Your change after buying a car is a $ {change}") # Your change after buying a car is a $ 2000
