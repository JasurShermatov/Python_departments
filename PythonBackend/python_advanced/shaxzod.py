import os
from datetime import datetime

users_file = 'users.txt'
user_orders_dir = 'orders/'

if not os.path.exists(user_orders_dir):
    os.makedirs(user_orders_dir)


def register_user():
    with open(users_file, 'a+') as f:
        f.seek(0)
        users = f.readlines()
        user_count = len(users) + 1
        name = input("Ismingizni kiriting: ")
        while True:
            username = input("Username kiriting: ")
            if username+'\n' in users:
                print("Bu username band. Qaytadan urinib ko'ring.")
            else:
                f.write(username + '\n')
                break
        print(f"Assalomu alaykum, {name}! Siz bizning {user_count}-foydalanuvchimizsiz.")
    return username


def show_menu():
    menu = {
        '1': ('Pizza', 50000),
        '2': ('Burger', 30000),
        '3': ('Sushi', 40000),
        '4': ('Salad', 20000),
        '5': ('Lavash', 25000)
    }
    print("Menyu:")
    for key, value in menu.items():
        print(f"{key}. {value[0]} - {value[1]} so'm")

    return menu


def take_order(username, menu):
    order_file = os.path.join(user_orders_dir, f"{username}.txt")
    with open(order_file, 'a') as f:
        while True:
            choice = input("Zakas qilmoqchi bo'lgan mahsulotning raqamini kiriting (tugatish uchun '0'): ")
            if choice == '0':
                break
            if choice in menu:
                item, price = menu[choice]
                f.write(f"{datetime.now()} - {item} - {price} so'm\n")
                print(f"{item} zakas qilindi.")
            else:
                print("Notog'ri raqam. Qaytadan urinib ko'ring.")


def show_history(username):
    order_file = os.path.join(user_orders_dir, f"{username}.txt")
    if os.path.exists(order_file):
        with open(order_file, 'r') as f:
            print(f"\n{username} buyurtma tarixi:")
            print(f.read())
    else:
        print("Siz hali hech narsa zakas qilmadingiz.")


def main():
    username = register_user()
    menu = show_menu()
    take_order(username, menu)
    show_history(username)


if __name__ == "__main__":
    main()
