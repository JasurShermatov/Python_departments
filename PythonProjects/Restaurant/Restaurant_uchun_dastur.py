# restaurant menu si uchun dastur!
class Restaurant:
    def __init__(self):
        self.menu = {
            "osh": 25,
            "lag'mon": 20,
            "shashlik": 30,
            "somsa": 10,
            "mastava": 15,
            "suyuq": 35,
            "norin": 40,
            "manti": 18,
            "salat": 12,
            "choy": 5
        }
        self.orders = {}

    def welcome(self):
        print("Assalomu alaykum Restaurantimizga hush helibsiz!")
        while (True):
            try:
                response = input("Iltimo tanlang: (1.mijoz/2.admin) ")
                if response == "mijoz" or response=="1":
                    self.customer_menu()
                elif response == "admin" or response=="2":
                    self.admin_login()
                else:
                    print("Noto'g'ri tanlov, iltimos, mijoz yoki admin deb tanlang.")
            except Exception as e:
                print("something is wrong")

    def customer_menu(self):
        print("Mijoz menyusi:")
        for index, item in enumerate(self.menu, start=1):
            print(f"{index}. {item} - {self.menu[item]} so'm")
        choice = int(input("Iltimos, tanlangan ovqat raqamini kiriting: "))
        if choice in range(1, len(self.menu) + 1):
            item = list(self.menu.keys())[choice - 1]
            self.place_order(item)
            self.order_again()
        else:
            print("Noto'g'ri tanlov, iltimos, mavjud raqamlardan birini tanlang.")

    def place_order(self, item):
        if item in self.orders:
            self.orders[item] += 1
        else:
            self.orders[item] = 1
        print(f"{item} buyurtmangiz qabul qilindi.")

    def order_again(self):
        again = input("Yana biror narsa buyurtma qilasizmi? (1.ha/2.yo'q): ")
        if again.lower() == "ha" or again.lower() == "1" :
            self.customer_menu()
        else:
            self.calculate_bill()
            self.orders.clear()

    def calculate_bill(self):
        total = sum(self.menu[item] * self.orders[item] for item in self.orders)
        print(f"Jami to'lov: {total} so'm. Haridingiz uchun rahmat!")

    def admin_login(self):
        while True:
            try:
                password = input("Parolni kiriting: ")

                if password == "2005" or password=="7777":
                    self.admin_menu()
                else:
                    print("Noto'g'ri parol, iltimos, qaytadan urinib ko'ring.")
                    self.admin_login()
            except Exception as e:
                print("Notog'ri parol kiritildi")


    def admin_menu(self):
        print("Admin menyusi:")
        print("1. Ovqat qo'shish")
        print("2. Ovqat olib tashlash")
        print("3. Ovqat narxlarni o'zgartirish")
        print("4. Jami ovqatlarni va narxlarni ko'rish")
        print("5. Chiqish")
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
            self.welcome()
            # print("Dasturdan chiqildi.")
        else:
            print("Noto'g'ri tanlov, iltimos, mavjud raqamlardan birini tanlang.")

    def add_dish(self):
        dish_name = input("Qo'shmoqchi bo'lgan yangi ovqatni nomini kiriting: ")
        price = int(input("Ovqat narxini kiriting: "))
        self.menu[dish_name] = price
        print(f"{dish_name} ovqati {price} so'mga qo'shildi.")
        self.admin_menu()

    def remove_dish(self):
        dish_name = input("Olib tashamoqchi bo'lgan ovqatni nomini kiriting: ")
        if dish_name in self.menu:
            del self.menu[dish_name]
            print(f"{dish_name} ovqati menudan olib tashlandi.")
        else:
            print("Bunday ovqat ro'yxatda mavjud emas.")
        self.admin_menu()

    def change_prices(self):
        print("Mavjud ovqatlar narxi:")
        for item in self.menu:
            print(f"{item} - {self.menu[item]} so'm")
        dish = input("Narxini o'zgartirmoqchi bo'lgan ovqatni tanlang: ")
        if dish in self.menu:
            new_price = int(input("Yangi narxni kiriting: "))
            self.menu[dish] = new_price
            print(f"{dish} ovqatining narxi {new_price} so'mga o'zgartirildi.")
        else:
            print("Bunday ovqat ro'yxatda mavjud emas.")
        self.admin_menu()

    def view_menu(self):
        print("Menu:")
        for item in self.menu:
            print(f"{item} - {self.menu[item]} so'm")
        self.admin_menu()

    def run(self):
        self.welcome()


restaurant = Restaurant()
restaurant.run()