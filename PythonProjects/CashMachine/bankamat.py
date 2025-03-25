import sys


class CashMachine:
    def __init__(self):
        self.balance = 0.0  # balance hozircha 0 ga teng

    def language(self):
        print("Choose the language/ O'zingizga qulay tilni tanlang")
        language = input("(1.English/2.Uzbek)\n>>>")
        if language == "1":
            self.admin_login_english()
        elif language == "2":
            self.admin_login_uzb()
        else:
            print("Unknown command ")
            self.language()  # Qaytadan til tanlashga urinib ko'radi.

    def admin_login_english(self):
        while True:
            try:
                password = input("Enter the pasword: ")

                if password in ["2005", "7777"]:
                    self.start_eng()
                    break
                else:
                    print("Incorrect pasword, please try again!.")
                    self.admin_login_english()
            except ValueError:
                print("You have entered incorrect password.")

    def admin_login_uzb(self):
        while True:
            try:
                parol = input("Parolni kiriting: ")

                if parol in ["7777", "2005"]:
                    self.start_uzb()
                    break
                else:
                    print("Noto'g'ri parol, iltimos, qaytadan urinib ko'ring.")
                    self.admin_login_uzb()
            except ValueError:
                print("Notog'ri parol kiritildi")

    def start_eng(self):
        while True:
            print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ️")
            print("♦️  ⚠️  CashMachine option             ♦️")
            print("♦️  1️⃣  See_balance                   ♦️")
            print("♦️  2️⃣  Add_balance                   ♦️")
            print("♦️  3️⃣  Withdraw_balance              ♦️")
            print("♦️  4️⃣  Exit                           ♦️")
            print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️")

            option = input("Choose the desired option\n>>>")
            if option == "1":
                self.see_balance_eng()
            elif option == "2":
                self.add_balance_eng()
            elif option == "3":
                self.withdraw_balance_eng()
            elif option == "4":
                self.admin_login_english()
            else:
                print("Incorrect option, choose again")

    def start_uzb(self):
        while True:
            print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ️")
            print("♦️  ⚠️  Bankamat optionlari!            ♦️")
            print("♦️  1️⃣  Hisob ni ko'rish               ♦️")
            print("♦️  2️⃣  hisobga pul qo'shish           ♦️")
            print("♦️  3️⃣  Hisobdan pul yechish           ♦️")
            print("♦️  4️⃣  Chiqish                         ♦️")
            print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️")

            option = input("Kerakli optionni tanlang\n>>>")
            if option == "1":
                self.see_balance_uzb()
            elif option == "2":
                self.add_balance_uzb()
            elif option == "3":
                self.withdraw_balance_uzb()
            elif option == "4":
                self.admin_login_uzb()
            else:
                print("Noto'g'ri option, qaytadan tanlang")

    def see_balance_eng(self):
        print(f"Your balance: {self.balance} sum")
        xoxlaysizmi = input("Would you like another operation (1.Yes/2.No)").lower()
        if xoxlaysizmi == "1":
            self.start_eng()
        elif xoxlaysizmi == "2":
            print("Thanks for using us!!!")
            sys.exit()

    def see_balance_uzb(self):
        print(f"Sizning balansingiz: {self.balance} so'm")
        xoxlaysizmi = input(
            "Yana boshqa operation bajarishni xoxlaysizmi (1.ha/2.yo'q)"
        ).lower()
        if xoxlaysizmi == "1":
            self.start_uzb()
        elif xoxlaysizmi == "2":
            print("Bizdan foydalanganingiz uchun tashakkur!!!")
            sys.exit()

    def add_balance_eng(self):
        try:
            amount = float(input("How much money you want to add?\n>>>"))
            if amount > 0:
                self.balance += amount
            else:
                print("Inter the correct amount")
            print(f"Your new balance: {self.balance} sum")
        except ValueError:
            print("Please enter the correct amount.")
        xoxlaysizmi = input("Would you like another operation? (1.Yes/2.No)").lower()
        if xoxlaysizmi == "1":
            self.start_eng()
        elif xoxlaysizmi == "2":
            print("Thanks for using us!!!")
            sys.exit()

    def add_balance_uzb(self):
        try:
            amount = float(input("Qancha pul qo'shmoqchisiz?\n>>>"))
            if amount > 0:
                self.balance += amount
            else:
                print("Iltimos tog'ri qiymat kiriting.")
            print(f"Sizning yangi balansingiz: {self.balance} so'm")
        except ValueError:
            print("Iltimos, to'g'ri miqdorni kiriting.")
        xoxlaysizmi = input(
            "Yana boshqa operation bajarishni xoxlaysizmi (1.ha/2.yo'q)"
        ).lower()
        if xoxlaysizmi == "1":
            self.start_uzb()
        elif xoxlaysizmi == "2":
            print("Bizdan foydalanganingiz uchun tashakkur!!!")
            sys.exit()

    def withdraw_balance_eng(self):
        try:
            amount = float(input("How much do you want to withdraw?\n>>>"))
            if amount > self.balance and amount > 0:
                print("There are insufficient funds in the balance.")
            else:
                self.balance -= amount
                print(f"Your new balance: {self.balance} sum")
        except ValueError:
            print("Unknown amount entered.")
            xoxlaysizmi = (
                input("Would you like another operation? (1.Yes/2.no)").lower().split()
            )
            if xoxlaysizmi == "1":
                self.start_eng()
            elif xoxlaysizmi == "2":
                print("Thanks for using us!!!")
                sys.exit()

    def withdraw_balance_uzb(self):
        try:
            amount = float(input("Qancha pul yechmoqchisiz?\n>>>"))
            if amount > self.balance and amount > 0:
                print("Balansda yetarli mablag' mavjud emas.")
            else:
                self.balance -= amount
                print(f"Sizning yangi balansingiz: {self.balance} so'm")
        except ValueError:
            print("Iltimos, to'g'ri miqdorni kiriting.")
            xoxlaysizmi = input(
                "Yana boshqa operation bajarishni xoxlaysizmi (1.ha/2.yo'q)"
            ).lower()
            if xoxlaysizmi == "1":
                self.start_uzb()
            elif xoxlaysizmi == "2":
                print("Bizdan foydalangningiz uchun raxmat!!!")
                sys.exit()

    def run(self):
        self.language()
        # self.admin_login_english()
        # self.admin_login_uzb()


if __name__ == "__main__":
    bankomat = CashMachine()
    bankomat.run()
