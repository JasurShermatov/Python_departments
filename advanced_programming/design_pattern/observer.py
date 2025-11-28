from abc import ABC, abstractmethod


class IObserver(ABC):
    @abstractmethod
    def update(self, price: int):
        pass


class IObservable(ABC):
    @abstractmethod
    def add_observer(self, obj: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, obj: IObserver):
        pass

    @abstractmethod
    def notify(self):
        pass


class Product(IObservable):
    def __init__(self, price: int):
        self.price = price
        self.__observers = []

    def change_price(self, price: int):
        self.price = price
        self.notify()

    def add_observer(self, obj: IObserver):
        self.__observers.append(obj)

    def remove_observer(self, obj: IObserver):
        self.__observers.remove(obj)

    def notify(self):
        for observer in self.__observers:
            observer.update(self.price)


class Buyer(IObserver):
    def __init__(self, obj: IObservable):
        self.obj = obj

    def update(self, price: int):
        if price > 550:
            print("This sale for buyer - {} $".format(price))


class WholeSale(IObserver):
    def __init__(self, obj: IObservable):
        self.obj = obj

    def update(self, price: int):
        if price > 300:
            print("This sale for wholesaler - {} $".format(price))


if __name__ == "__main__":
    product = Product(1000)
    whole_sale = WholeSale(product)
    buyer = Buyer(product)

    product.add_observer(whole_sale)
    product.add_observer(buyer)

    product.change_price(600)