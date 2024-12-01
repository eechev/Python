# def greet():
#     name = input("What is your name? ")
#     print(f"Hello, {name}")
    
    
# greet()

def calculate_mgp(car):
    mpg = car['mileage'] / car['fuel_consumed']
    return mpg


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


def print_car_info(car):
    mpg = calculate_mgp(car)
    name = car_name(car)
    print(f"{name} gets {mpg} miles per gallon")

cars = [
    {
        "make": "Ford",
        "model": "Mustang",
        "mileage": 30000,
        "fuel_consumed": 500
    },
    {
        "make": "Chevrolet",
        "model": "Camaro",
        "mileage": 30000,
        "fuel_consumed": 800
    }
]


for car in cars:
    print_car_info(car)
    