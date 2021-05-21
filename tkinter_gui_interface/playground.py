def add(*args): # this is a tuple
    total = 0
    for n in args:
        total += n
    return total

print(add(3,4,5,6,7,8,10,33))

def dict_add(**kwargs): # this is a dictionary
    print(kwargs)

dict_add(width=10, height=10, size="640x480")

class Car:

    def __init__(self, **kwargs):
        self.model = kwargs.get("model")
        self.make = kwargs.get("make")

car = Car(make=True, model="Peugout")
print(car.model, car.make)