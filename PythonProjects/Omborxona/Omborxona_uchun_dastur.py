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
        for i,x in self.mahsulotlar.items():
            if self.mahsulotlar[i]!=0:
            # print(f"{mahsulot_nomi} mahsulotidan qolgan miqdori: {self.mahsulotlar[mahsulot_nomi]} ta")
                print(f"{i} dan {x} ta qolgan")
    def qolmagan_mahsulotlar(self):
        qolmaganlar = [mahsulot for mahsulot, miqdor in self.mahsulotlar.items() if miqdor == 0]
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





