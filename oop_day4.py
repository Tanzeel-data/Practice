class car:
    def __init__(self, model, brand , colour):
        self.model = model
        self.brand = brand
        self.colour = colour
    
    def start(self):
        print("car is starting")
    
    def info(self):
        print(f"model: {self.model},\n brand: {self.brand},\n colour: {self.colour}")

car1 = car("1995", "BMW", "black")
car1.start()
car1.info()

