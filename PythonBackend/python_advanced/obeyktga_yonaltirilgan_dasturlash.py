# class Student:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def fullname(self):
#         return "John Smith"
#
#
# Student_=Student.fullname("John Smith")
# print(Student_)


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "You can't divide by zero"


while True:
    try:
        a = float(input("Birinchi sonni kiriting\n>>> "))
        print("Amallardan birini tanlang! (1.+, 2.-, 3.*, 4./)")
        amal = input("Tanlang: ")
        b = float(input("Ikkinchi sonni kiriting\n>>> "))

        if amal == "1" or amal == "+":
            print("Natija: ", Calculator.add(a, b))
        elif amal == "-" or amal == "2":
            print("Natija: ", Calculator.subtract(a, b))
        elif amal == "*" or amal == "3":
            print("Natija: ", Calculator.multiply(a, b))
        elif amal == "/" or amal == "4":
            print("Natija: ", Calculator.divide(a, b))
        else:
            print("Noma'lum amal")
    except ValueError:
        print("Noma'lum kiritish. Iltimos, raqam kiriting.")

    davom_etish = input("Dastur ishlashda davom etsinmi? (ha/yo'q): ").strip().lower()
    if davom_etish != "ha":
        print("Dastur to'xtatildi.")
        break
