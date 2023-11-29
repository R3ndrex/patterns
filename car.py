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
        del self.cars[car_name]
        return change

carshowroom1 = CarShowroom()
carshowroom1.add_car("Bugatti", 5000)
available_cars = carshowroom1.get_available_cars()
print(available_cars) # ["Bugatti"]

carshowroom = CarShowroom()
available_cars = carshowroom.get_available_cars()
print(available_cars) # ["Bugatti"]

carshowroom.add_car("Toyota", 4600)
available_cars = carshowroom.get_available_cars()
print(available_cars) # ["Bugatti","Toyota"]
change = carshowroom.buy_car("Bugatti", 7000) 
print(f"Your change after buying a car is a $ {change}") # Your change after buying a car is a $ 2000
available_cars = carshowroom.get_available_cars()
print(available_cars) # Bugatti
