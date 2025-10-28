from functools import wraps
from abc import ABC, abstractmethod
#
# def decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Before")
#         result = func(*args, **kwargs)
#         print("After")
#         return result
#     return wrapper
#
# @decorator
# def add(x, y):
#     return x + y



class ICoffee(ABC):
    @abstractmethod
    def cost(self):
        raise NotImplemented


class SimpleCoffee(ICoffee):
    def cost(self):
        return 10

class CoffeeDecorator(ICoffee):
    def __init__(self, coffee: ICoffee):
        self.coffee = coffee


    @abstractmethod
    def cost(self):
        raise NotImplemented


class MilkCoffee(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 5

class ChocolateCoffee(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 7

if __name__ == '__main__':
    simple_coffee = SimpleCoffee()
    milk_coffee = MilkCoffee(simple_coffee)
    chocolate_coffee = ChocolateCoffee(simple_coffee)
    print(chocolate_coffee.cost())

