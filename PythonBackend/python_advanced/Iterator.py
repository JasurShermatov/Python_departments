# # my_list = [1,2,3,4,5,6,7,8,9]
# # # iterable?
# # iterator = iter(my_list)
# # while True:
# #     try:
# #         element = next(iterator)
# #     except StopIteration:
# #         break
# #     print(element)
#
#
#
# class Counter:
#     def __init__(self, count: int):
#         self.i = -1
#         self.count = count
#
#     def __iter__(self):
#         print("got iter call")
#         return self
#
#     def __next__(self):
#         print("got next call")
#         self.i += 1
#         if self.i == self.count:
#             print("raised StopIteration")
#             raise StopIteration
#         return self.i
#
#
# counter = Counter(5)
# for c in counter:
#     print(c)
#
#
#
#
# # import itertools
# # for _ in itertools.count():
# #     print("This loop will run forever")
#
#
# # tuple = ("apple", "banana", "cherry")
# # iterator = iter(tuple)
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# #


from decimal import Decimal


class Calculator:
    def __init__(self, num1: int | float, num2: int | float) -> None:
        self.num1 = Decimal(num1)
        self.num2 = Decimal(num2)

    @property
    def add(self) -> Decimal:
        return self.num1 + self.num2

    @property
    def subtract(self) -> Decimal:
        return self.num1 - self.num2

    @property
    def multiply(self) -> Decimal:
        return self.num1 * self.num2

    @property
    def divide(self) -> Decimal | str:
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Division by zero"

    def __str__(self) -> str:
        return f"Calculating by {self.num1} {self.num2}"

    def __repr__(self) -> str:
        return f"Calculating by {self.num1} {self.num2}"

    def __eq__(self, other) -> bool:
        return self.num1 == other.num1 and self.num2 == other.num2

    def __ne__(self, other) -> bool:
        return self.num1 != other.num1 and self.num2 != other.num2

    def __lt__(self, other) -> bool:
        return self.num1 < other.num1 and self.num2 < other.num2

    def __le__(self, other) -> bool:
        return self.num1 <= other.num1 and self.num2 <= other.num2

    def __gt__(self, other) -> bool:
        return self.num1 > other.num1 and self.num2 > other.num2

    def __ge__(self, other) -> bool:
        return self.num1 >= other.num1 and self.num2 >= other.num2


def get_number() -> float:
    while True:
        try:
            user_input = float(input("Enter a number: "))
            return user_input
        except ValueError:
            print("Please enter a number")


def get_opration() -> int:
    while True:
        try:
            user_input = int(input("Enter a operation: "))
            return user_input
        except ValueError:
            print("Please enter a number")


def menu() -> None:
    print("Select an operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Changing first number")
    print("6.Changing first number")
    print("7.Exit")


def main():
    try:
        num1 = get_number()
        num2 = get_number()
        while True:
            result = Calculator(num1, num2)
            menu()
            operation = get_opration()
            match operation:
                case 1:
                    print(result.add)
                case 2:
                    print(result.subtract)
                case 3:
                    print(result.multiply)
                case 4:
                    print(result.divide)
                case 5:
                    old_num = num1
                    num1 = get_number()
                    print(f"{old_num} -> {num1}")
                case 6:
                    old_num = num2
                    num2 = get_number()
                    print(f"{old_num} -> {num2}")
                case 7:
                    break
    except KeyboardInterrupt:
        print("\nBye")


if __name__ == "__main__":
    main()
