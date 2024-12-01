class MyCustomError(TypeError):
    """ Custom error class """
    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}")
        self.code = code

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def __repr__(self):
        return f"<Car: {self.make} {self.model}>"

class Garage:
    def __init__(self):
        self.cars = []
        
    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        if not isinstance(car, Car):
            raise MyCustomError(f"You are trying to add a {car} of type '{car.__class__.__name__}', but the car must be of type 'Car'", 500)

        print(f"Adding {car} to the garage")
        self.cars.append(car)
    
myGarage = Garage()
try:
    myGarage.add_car(Car('Ford', 'Mustang'))
    myGarage.add_car(Car("Chevrolet", "Camaro"))
    myGarage.add_car('Mustang')
except MyCustomError as e:
    print(f"Error: The car must be of type 'Car' with error code {e.code}")
finally:
    print(f"The garage now has a total of {len(myGarage)} cars")
