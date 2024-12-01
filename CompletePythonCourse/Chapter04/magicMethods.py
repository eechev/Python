class Garage:
    def __init__(self):
        self.cars = []
        
    def __len__ (self):
        return len(self.cars)
    
    def __getitem__ (self, index) :
        return self.cars[index]
    
    def __repr__(self):
        return f'<Garage {self.cars}>'
    
    def __str__(self):
        return f'Garage with {len(self)} cars'
    
    def addCar(self, car):
        self.cars.append(car)
        
        
ford = Garage()
ford.addCar('Fiesta')
ford.addCar('Mustang')
print(f"Your garage has {len(ford)} cars")

print(f"Your first car is {ford[0]}")


for car in ford:
    print(car)
    
print(ford)

