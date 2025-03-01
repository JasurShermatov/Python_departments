from datetime import datetime, timedelta

# print(datetime.today().strftime("%m/%d/%Y"))

# yesterday = datetime.now() + timedelta(days=1)
# print(yesterday)


# from decimal import Decimal
# print(Decimal("0.1") + Decimal("0.2"))  # agarda decimilda foydalanmasdan oddiy float ko'rinishida bersak bu bizga 0.3 yaniq aniq son chiqarib bermaydi
#

# from random import sample
#
# names = ["Jasur", "Feruz", "Javohir"]
# selected_names = sample(names, 3)
# print(f"<<{selected_names[0]}> va <{selected_names[1]}>> bir jamoda o'ynaydi\n<<{selected_names[2]}>> ularga qarshi o'ynaydi")




# from random import shuffle, choice
# names = ["Python", "Java", "C", "C++", "JavaScript"]
# name = choice(names)
# print(name)



# import itertools
# l1 = ["python", "Java", "c"]
# l2 = ["django", "spring", "gr"]
# for i in itertools.zip_longest(l1, l2):
#     print({i})


import calendar
while True:
    try:
        year = int(input("Enter year: "))
        break
    except ValueError:
        print("Faqat son kiriting, qaytadan urinib ko'ring")

print(calendar.calendar(year))
