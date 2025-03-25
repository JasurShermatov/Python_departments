# bank hisobingizi ko'ra oladigan dasturcha
bank_account = 1000000000


def bank_account_login():
    my_pasword = "12345"
    urinishlar = 3
    while urinishlar > 0:
        print("Sizda kirish uchun 3 ta imkonyat bor!")
        password_input = input("Parolni kiriting: ")
        if password_input == my_pasword:
            print("Kirish muvaffaqiyatli amalga oshdi!")
            print(f"Hisobingizda quydagi summa mavjud! {bank_account:,}$")
            break
        else:
            urinishlar -= 1

            print(
                "Noto'g'ri parol kiritildi! iltimos tekshirib qaytadan urinib ko'ring!"
            )
            print(f"Sizda qoldi {urinishlar} dona urinish")
            print("Kirish imkonsiz")


bank_account_login()


# Xona deraza va eshik o'lchamlarini kiritasi bu esa sizga qancha kraska ketishini hisoblaydi
print("siz devor necha km ekanligini hisoblab qancha bo'yoq ketganini hisoblang")
eni = float(input("Devor eninni kiriting="))
boyi = float(input("Devor boyini kiritng="))
balandlik = float(input("Devor balandligini kiriting="))
deraza_soni = int(input("Derazalar sonini kirit="))
deraza_eni = float(input("Deraza enini kiriting="))
deraza_boyi = float(input("Deraza boyini kiriting="))
eshiklar_soni = int(input("Eshiklar sonini kiriting="))
eshik_eni = float(input("Eshik enini kiriting="))
eshik_boyi = float(input("Eshik boyini kiriting="))
devor = (eni * balandlik + boyi * balandlik) * 2
harajatlar = float(input("Enter the price of kraska:="))

deraza = deraza_eni * deraza_boyi * deraza_soni
eshik = eshik_eni * eshik_boyi * eshiklar_soni
hajm = (devor - deraza - eshik) / 0.6
javop = hajm * harajatlar
print(f" Sizga {javop} so'm kerak bo'ladi xonani bo'yash uchun")


# Radar uchun dastur 3 xil turdagi istisno davlat raqamlariga jarima yozmaydi
def jarima_yoz():
    nomer = input("Please, enter the number: ")

    if nomer.endswith("VSP") or nomer.endswith("PPP"):
        print(" Jarima yozma bu davlat raqami:")
    elif nomer.count("X") >= 2 and nomer.endswith("XX"):
        print("Jarima yozma bu davlat raqami:")
    else:
        print("Jarima yoz bu davlat raqami emas")


# Omborxona uchun dastur
class Ombor:
    def __init__(self):
        self.mahsulotlar = {}

    def start(self):
        print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️")
        print("♦️  ⚠️  Ombor bo'limlari                                  ♦️")
        print("♦️  1️⃣  Mahsulot qo'shish                                 ♦️")
        print("♦️  2️⃣  Mahsulot yangilash                                ♦️")
        print("♦️  3️⃣  mahsulot qancha borligini chiqarish               ♦️")
        print("♦️  4️⃣  qolmagan mahsulotlarni chiqarish                  ♦️")
        print("♦️  5️⃣  chiqish                                           ♦️")
        print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️")

    def mahsulot_qoshish(self):
        mahsulot_nomi = input("Mahsulot nomini kiriting: ")
        if mahsulot_nomi in self.mahsulotlar:
            print(f"{mahsulot_nomi} allaqachon kiritilgan")
        else:
            miqdori = int(input("Miqdorini kiriting: "))
            self.mahsulotlar[mahsulot_nomi] = miqdori

    def mahsulot_update_qilish(self):
        mahsulot_nomi = input("Mahsulot nomini kiriting: ")
        if mahsulot_nomi in self.mahsulotlar:
            yangi_miqdor = int(input("Yangi miqdorni kiriting: "))
            self.mahsulotlar[mahsulot_nomi] = yangi_miqdor
        else:
            print(f"{mahsulot_nomi} nomli mahsulot topilmadi.")

    def mahsulot_qolganligi(self):
        # mahsulot_nomi = input("Mahsulot nomini kiriting: ")
        for i, x in self.mahsulotlar.items():
            if self.mahsulotlar[i] != 0:
                # print(f"{mahsulot_nomi} mahsulotidan qolgan miqdori: {self.mahsulotlar[mahsulot_nomi]} ta")
                print(f"{i} dan {x} ta qolgan")

    def qolmagan_mahsulotlar(self):
        qolmaganlar = [
            mahsulot for mahsulot, miqdor in self.mahsulotlar.items() if miqdor == 0
        ]
        print(f"Qolmagan mahsulotlar: {', '.join(qolmaganlar)}")


def main():
    system = Ombor()
    while True:
        system.start()
        choice = input("Variantni tanlang: ")

        if choice == "1":
            system.mahsulot_qoshish()
        elif choice == "2":
            system.mahsulot_update_qilish()
        elif choice == "3":
            system.mahsulot_qolganligi()
        elif choice == "4":
            system.qolmagan_mahsulotlar()
        elif choice == "5":
            print("Tizimdan chiqildi. Xayr!")
            break
        else:
            print("Notog'ri variant. Qayta urinib ko'ring")


if __name__ == "__main__":
    main()


# restaurant menu si uchun dastru
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
            "choy": 5,
        }
        self.orders = {}

    def welcome(self):
        print("Assalomu alaykum Restaurantimizga hush helibsiz!")
        while True:
            try:
                response = input("Iltimo tanlang: (1.mijoz/2.admin) ")
                if response == "mijoz" or response == "1":
                    self.customer_menu()
                elif response == "admin" or response == "2":
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
        if again.lower() == "ha" or again.lower() == "1":
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

                if password == "2005" or password == "7777":
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


def fibonacci(number: int) -> int:
    if number < 2:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(int(input("Enter a number: "))))
