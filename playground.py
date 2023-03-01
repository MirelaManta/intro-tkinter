# Create an add function that takes an unlimited/ unspecified number of arguments

def add(*args):
    # args will be a tuple
    print(args[0])

    sum = 0
    for number in args:
        sum += number
    return sum


print(add(8, 7, 9, 3, 5, 13, 1, 12))


def calculate(n, **kwargs):
    # this means I am creating an unlimited number of keyword arguments
    print(kwargs)  # will be a dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        # the benefit of get (instead of kw["make"]) is that if the key doesn't exist in the dictionary,
        # it will just return None and won't give us an error
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)