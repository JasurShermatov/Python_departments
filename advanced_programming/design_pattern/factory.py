from abc import ABC, abstractmethod


class ToyABC(ABC):
    @abstractmethod
    def play(self):
        pass


class Car(ToyABC):
    def play(self):
        print("Playing with a car")


class Doll(ToyABC):
    def play(self):
        print("Playing with a doll")


TOY_VARIANTS = {
    "car": Car(),
    "doll": Doll(),
}


class ToyFactory:

    @staticmethod
    def create_toy(toy):
        if toy in TOY_VARIANTS:
            return TOY_VARIANTS[toy].play()
        raise ValueError(f"Unknown toy variant: {toy}")


if __name__ == "__main__":
    ToyFactory.create_toy("car")
    ToyFactory.create_toy("doll")