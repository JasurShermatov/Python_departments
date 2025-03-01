import random


class GameOver(Exception):
    pass


def random_number(): return random.randint(1, 20)


def check_number(number, guess):

    message = "Men o'ylagan son"
    if number < guess: return f"{message} {guess} dan kichikroq."
    if number > guess: return f"{message} {guess} dan kattaroq."
    raise GameOver


def main():
    number = random_number()
    print("Men 1-20 oralig'ida bir son o'yladim!")

    attempts = 3
    while True:
        attempts -= 1
        if attempts == -1:print(f"sizda boshqa imkon qolmadi !\n Siz yutqazdingiz.\n Men o'ylagan son {number} edi."); break;
        try:
            guess = int(input(f"{3 - attempts}- taxminingni kiriting\n>>>"))
            message = check_number(number, guess)
            print(message)


        except GameOver:
            print("Siz o'ylagan sonni topdingiz, o'yin tugadi!"); break


if __name__ == "__main__": main()






