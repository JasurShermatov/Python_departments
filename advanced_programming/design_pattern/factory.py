from abc import ABC, abstractmethod


class ToyABC(ABC):
    @abstractmethod
    def create(self):
        pass


class Car(ToyABC):
    def create(self):
        print("Created car")


class Doll(ToyABC):
    def create(self):
        print("Created doll")


class ToyFactoryABC(ABC):
    @abstractmethod
    def build_toy(self):
        pass

    def build(self):
        toy = self.build_toy()
        return f'Building toy {toy.create()}'


class CarFactory(ToyFactoryABC):
    def build_toy(self):
        return Car()


class DollFactory(ToyFactoryABC):
    def build_toy(self):
        return Doll()


if __name__ == '__main__':
    car = CarFactory()
    car.build()
    dool = DollFactory()
    dool.build()