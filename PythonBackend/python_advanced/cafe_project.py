import os
from datetime import datetime


class Cafe:
    def __init__(self):
        self.food_menu = {
            "ChisBurger": 35000,
            "Burger": 30000,
            "Lavash": 25000,
            "Sushi": 30000,
            "Salad": 20000,
            "Sendvich": 15000,
            "Doner": 35000,
            "Clup": 18000,
        }
        self.drinks_menu = {
            "Choy": 5000,
            "Kofe": 10000,
            "Suv": 2000,
            "Cola": 8000,
            "Fanta": 8000,
            "Sprite": 8000,
        }
        self.orders = {}
        self.users_file = 'users.txt'
        self.user_orders_dir = 'orders/'
        if not os.path.exists(self.user_orders_dir):
            os.makedirs(self.user_orders_dir)

    def welcome(self):
        print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ")
        print("♦️  Assalomu alaykum Cafeyimizga hush kelibsiz!              ♦️")
        print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️")
        while True:
            try:
                response = input("Iltimos tanlang: (1. mijoz/2. admin)\n>>> ")
                if response == "mijoz" or response == "1":
                    self.customer_menu()
                elif response == "admin" or response == "2":
                    self.admin_login()
                else:
                    print("Noto'g'ri tanlov, iltimos, mijoz yoki admin ni tanlang!")
            except Exception as e:
                print("Xato yuz berdi: ", e)

    def register_user(self):
        if not os.path.exists(self.users_file):
            open(self.users_file, 'w').close()

        with open(self.users_file, 'r') as f:
            users = f.readlines()
        user_count = len(users) + 1
        name = input("Ismingizni kiriting: ")
        while True:
            username = input("Username kiriting: ")
            if username + '\n' in users:
                print("Bu username band. Qaytadan urinib ko'ring.")
            else:
                with open(self.users_file, 'a') as f:
                    f.write(username + '\n')
                break
        print(f"Assalomu alaykum, {name}! Siz bizning {user_count}-foydalanuvchimizsiz.")
        return username

    def customer_menu(self):
        username = self.register_user()
        while True:

            print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️  ♦️  ♦️  ️")
            print("♦️  ⚠️  Mijoz menyusi:                   ♦️")
            print("♦️  1️⃣  Ovqat buyurtma qilish:           ♦️")
            print("♦️  2️⃣  Ichimlik buyurtma qilish:        ♦️")
            print("♦️  3️⃣  Buyurtmani yakunlash:            ♦️")
            print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️  ")

            choice = int(input("Iltimos, tanlovni kiriting: "))
            if choice == 1:
                self.show_food_menu(username)
            elif choice == 2:
                self.show_drinks_menu(username)
            elif choice == 3:
                self.calculate_bill(username)
                break
            else:
                print(" ♦️Noto'g'ri tanlov, iltimos, mavjud raqamlardan birini tanlang ♦️")

    def show_food_menu(self, username):
        print("Ovqat menyusi:")
        for index, item in enumerate(self.food_menu, start=1):
            print(f"{index}. {item} - {self.food_menu[item]} so'm")
        self.take_order(username, self.food_menu)

    def show_drinks_menu(self, username):
        print("Ichimliklar menyusi:")
        for index, item in enumerate(self.drinks_menu, start=1):
            print(f"{index}. {item} - {self.drinks_menu[item]} so'm")
        self.take_order(username, self.drinks_menu)

    def take_order(self, username, menu):
        while True:
            choice = int(input("Iltimos, tanlangan raqamni kiriting (tugatish uchun 0): "))
            if choice == 0:
                break
            if choice in range(1, len(menu) + 1):
                item = list(menu.keys())[choice - 1]
                self.place_order(username, item, menu[item])
            else:
                print("Noto'g'ri tanlov, iltimos, mavjud raqamlardan birini tanlang.")

    def place_order(self, username, item, price):
        order_file = os.path.join(self.user_orders_dir, f"{username}.txt")
        with open(order_file, 'a') as f:
            f.write(f"{datetime.now()} - {item} - {price} so'm\n")
        if item in self.orders:
            self.orders[item] += 1
        else:
            self.orders[item] = 1
        print(f"{item} buyurtmangiz qabul qilindi.")

    def calculate_bill(self, username):
        total = sum((self.food_menu.get(item, 0) + self.drinks_menu.get(item, 0)) * self.orders[item] for item in self.orders)
        print(f"Jami to'lov: {total} so'm. Haridingiz uchun rahmat!")
        self.orders.clear()

    def admin_login(self):
        while True:
            try:
                password = input("Parolni kiriting: ")
                if password == "2005" or password == "7777" or password == "1111":
                    self.admin_menu()
                else:
                    print("Noto'g'ri parol, iltimos, qaytadan urinib ko'ring.")
            except Exception as e:
                print("Xato yuz berdi: ", e)

    def search_customer_history(self):
        username = input("Username ni qidiring: ")
        order_file = os.path.join(self.user_orders_dir, f"{username}.txt")
        if os.path.exists(order_file):
            with open(order_file, 'r') as f:

                print(f"♦️{username}   buyurtma tarixi:♦️")
                print(f.read())
        else:
            print(f"{username} ga oid hech qanday buyurtma topilmadi.")

    def admin_menu(self):
        while True:

            print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️  ♦️ ")
            print("♦️  ⚠️  Admin menyusi:                             ♦️")
            print("♦️  1️.  Ovqat qo'shish:                            ♦️")
            print("♦️  2️.  Ovqat olib tashlash:                       ♦️")
            print("♦️  3️.  Ovqat narxlarini o'zgartirish:             ♦️")
            print("♦️  4️.  Jami ovqatlarni va narxlarni ko'rish:      ♦️")
            print("♦️  5️.  Mijozlar tarixini ko'rish:                 ♦️")
            print("♦️  6.   Chiqish:                                  ♦️")
            print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️  ♦️ ️")

            choice = int(input("Tanlov raqamini kiriting: "))
            if choice == 1:
                self.add_dish()
            elif choice == 2:
                self.remove_dish()
            elif choice == 3:
                self.change_prices()
            elif choice == 4:
                self.view_menu()
            elif choice == 5:
                self.search_customer_history()
            elif choice == 6:
                self.welcome()
            else:
                print("Noto'g'ri tanlov, iltimos, mavjud raqamlardan birini tanlang.")

    def add_dish(self):
        dish_type = input("Qo'shmoqchi bo'lgan menyu turi (1. Ovqat / 2. Ichimlik): ")
        dish_name = input("Qo'shmoqchi bo'lgan yangi nomini kiriting: ")
        price = int(input("Narxini kiriting: "))
        if dish_type == "1":
            self.food_menu[dish_name] = price
        elif dish_type == "2":
            self.drinks_menu[dish_name] = price
        else:
            print("Noto'g'ri tanlov. Iltimos, ovqat yoki ichimlik tanlang.")
            return
        print(f"{dish_name} menyuga {price} so'mga qo'shildi.")

    def remove_dish(self):
        dish_type = input("Olib tashamoqchi bo'lgan menyu turi (1. Ovqat / 2. Ichimlik): ")
        dish_name = input("Olib tashamoqchi bo'lgan nomini kiriting: ")
        if dish_type == "1" and dish_name in self.food_menu:
            del self.food_menu[dish_name]
        elif dish_type == "2" and dish_name in self.drinks_menu:
            del self.drinks_menu[dish_name]
        else:
            print("Bunday nom ro'yxatda mavjud emas.")
            return
        print(f"{dish_name} menudan olib tashlandi.")

    def change_prices(self):
        print("Mavjud menyu:")
        for item in {**self.food_menu, **self.drinks_menu}:
            print(f"{item} - {self.food_menu.get(item, self.drinks_menu.get(item))} so'm")
        dish_name = input("Narxini o'zgartirmoqchi bo'lgan nomini tanlang: ")
        if dish_name in self.food_menu or dish_name in self.drinks_menu:
            new_price = int(input("Yangi narxni kiriting: "))
            if dish_name in self.food_menu:
                self.food_menu[dish_name] = new_price
            else:
                self.drinks_menu[dish_name] = new_price
            print(f"{dish_name} narxi {new_price} so'mga o'zgartirildi.")
        else:
            print("Bunday nom ro'yxatda mavjud emas.")

    def view_menu(self):
        print("Ovqat menyusi:")
        for item in self.food_menu:
            print(f"{item} - {self.food_menu[item]} so'm")
        print("Ichimliklar menyusi:")
        for item in self.drinks_menu:
            print(f"{item} - {self.drinks_menu[item]} so'm")

    def view_order_history(self):
        for filename in os.listdir(self.user_orders_dir):
            with open(os.path.join(self.user_orders_dir, filename), 'r') as f:
                print(f"{filename} tarix:")
                print(f.read())

    def run(self):
        self.welcome()


restaurant = Cafe()
restaurant.run()
