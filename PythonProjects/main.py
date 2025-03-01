username = "jasur_0528"
parol = "2005"


def login():
    while True:
        a = input("Username kiriting: ")
        b = input("Parolni kiriting: ")
        if a == parol and b == username:
            print("Mavaffaqyatli kirdingiz")
            break
        else:
            print("Parol yoki username xato")


def main() -> None:
    login()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nDastur to'xtatildi")
    except Exception as e:
        print(f"\nXatolik yuz berdi: {e}")
