from abc import ABC, abstractmethod
from datetime import datetime


class ParkingSpot(ABC):
    def __init__(self, spot_id: int, is_free: bool = True):
        self.id = spot_id
        self.is_free = is_free

    def get_is_free(self) -> bool:
        return self.is_free


class Vehicle(ABC):
    def __init__(self, license_no: str):
        self.__license_no = license_no

    @abstractmethod
    def assign_ticket(self):
        pass


class Payment(ABC):
    def __init__(self, amount: float, status: str, timestamp: datetime):
        self.__amount = amount
        self.__status = status
        self.__timestamp = timestamp

    @abstractmethod
    def initiate_transaction(self):
        pass


class CashPayment(Payment):
    def __init__(self, amount: float, status: str, timestamp: datetime):
        super().__init__(amount, status, timestamp)

    def initiate_transaction(self):
        print("Cash payment initiated")


class CreditCardPayment(Payment):
    def __init__(
        self, amount: float, status: str, timestamp: datetime, card_number: str
    ):
        super().__init__(amount, status, timestamp)
        self.card_number = card_number

    def initiate_transaction(self):
        print("Credit card payment initiated")


class Car(Vehicle):
    def assign_ticket(self):
        print("Ticket assigned to Car")


class Truck(Vehicle):
    def assign_ticket(self):
        print("Ticket assigned to Truck")


class MotorCycle(Vehicle):
    def assign_ticket(self):
        print("Ticket assigned to Motorcycle")


class Van(Vehicle):
    def assign_ticket(self):
        print("Ticket assigned to Van")


class ParkingTicket:
    def __init__(
        self,
        ticket_no: int,
        timestamp: datetime,
        exit_time: datetime = None,
        amount: float = 0,
        payment: Payment = None,
    ):
        self.__ticket_no = ticket_no
        self.__timestamp = timestamp
        self.__exit_time = exit_time
        self.__amount = amount
        self.__payment = payment


class Entrance:
    def __init__(self, entrance_id: int):
        self.__id = entrance_id

    def get_ticket(self) -> ParkingTicket:
        return ParkingTicket(ticket_no=1, timestamp=datetime.now())


class Exit:
    def __init__(self, exit_id: int):
        self.__id = exit_id

    def validate_ticket(self):
        print("Ticket validated")


class ParkingLot:
    def __init__(self, lot_id: int, name: str, address: str):
        self.__id = lot_id
        self.__name = name
        self.__address = address

    def get_parking_ticket(self) -> ParkingTicket:
        return ParkingTicket(ticket_no=1, timestamp=datetime.now())

    def is_full(self) -> bool:
        return False


class Account(ABC):
    def __init__(self, username: str, password: str, status: str, person: str):
        self.__username = username
        self.__password = password
        self.__status = status
        self.__person = person

    @abstractmethod
    def reset_password(self):
        pass


class DisplayBoard:
    def __init__(self, id_parking: int, parking_spots: dict):
        self.id = id_parking
        self.parking_spots = parking_spots

    def add_parking_spot(self, parking_spot: ParkingSpot):
        self.parking_spots[parking_spot.id] = parking_spot

    def show_free_spot(self):
        for spot in self.parking_spots.values():
            if spot.get_is_free():
                print(f"Spot {spot.id} is free")


class Admin(Account):
    def __init__(self, username: str, password: str, status: str, person: str):
        super().__init__(username, password, status, person)

    def add_parking_spot(self, parking_spot: ParkingSpot) -> bool:
        print("Parking spot added")
        return True

    def add_display_board(self, display_board: DisplayBoard) -> bool:
        print("Display board added")
        return True

    def add_entrance(self, entrance: Entrance) -> bool:
        print("Entrance added")
        return True

    def add_exit(self, exit_gate: Exit) -> bool:
        print("Exit added")
        return True

    def reset_password(self):
        print("Password reset")


class ParkingAgent(Account):
    def process_ticket(self) -> bool:
        print("Ticket processed")
        return True


class ParkingRate:
    def __init__(self, hours: float, rate: float):
        self.hours = hours
        self.rate = rate

    def calculate(self):
        return self.hours * self.rate
