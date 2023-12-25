class ProductionManager:
    _instance = None
    def __new__(cls, price, title,amount):
        if not cls._instance:
            cls._instance = super(ProductionManager, cls).__new__(cls)
            cls._instance.price = price
            cls._instance.title = title
            cls._instance.amount = amount
        return cls._instance

product1 = ProductionManager(12.99, "Fanta", 1000)
print("Cost:", product1.price)
print("Title:", product1.title)
print("Amount:", product1.amount)

product2 = ProductionManager(9.99, "Coca-Cola", 9201)
print("Cost:", product2.price)  # 12.99
print("Title:", product2.title)  # Fanta
print("Amount:", product2.amount)  # 1000

print(product1 is product2)  # True
