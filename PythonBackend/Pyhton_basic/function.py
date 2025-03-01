# def ask_name():
#     return input("What is your name? ")
# name_one = ask_name()


# print(input("What is your name? "))
# def send_email(to, text):
#     return f" to= {to}\ntext= {text}"
#     # print("to", to)
#     # print("text", text)
#
#
# print(send_email("shermatovjasur800@gmail.com", "hello every one"))


# def send_email(to, text, **kwargs):
#     print("to", to)
#     print("text", text)
#     print("name", kwargs["name"])
#     print(type(kwargs))
#
#
# send_email("shermatovjasur800@gmail.com", "this is text", name="shermatovjasur")


# def send_email(to, text, bcc=''):
#     print("to", to)
#     print("text", text)
#     print("bcc", bcc)
#
#
# send_email("shermatovjasur800@gmail.com", "this is text","@gmail.com")


# def square(n):
#     ''' takes a number and returns n*n'''
#     return n*n
#
#
# print(square(5))
# help(square)


# def g_v():
#     global A
#     A = 65
#     print("hello world", A)
#
#
# def g_v_v():
#     print(A)
# g_v()
# g_v_v()


# add = lambda a,b: a*b
# print(add(5,2))


# '''
#         lamda orqaliham functionga o'xshab foydalanishimiz mumkin faqatgina 1 qatorga yozishimiz mumkin
# '''
# cube = lambda x: x**3
# print(cube(5))


# def name(name):
#     return f" hello {name}"
# print(name(input("Enter your name?\n>>>")))






# def factorial(num):
#     """bu yerda esa function yordamida kishik factarial hioblaydigan dastur"""
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)
#
#
# a = int(input("Enter num: "))
# print(factorial(a))




# def check_maximal(*names):
#     if not names:
#         return "kamida bitta ism kiriting"
#     maximal=len(names[0])
#     maximal_num= names[0]
#     for nume in names:
#         if len(nume)>maximal:
#             maximal=len(nume)
#             maximal_num= nume
#     return maximal_num
# print(check_maximal("shaxzod", "jasur"))




# def check_minimal(*names):
#     if not names:
#         return "kamida bitta ism kiriting"
#     manimum=len(names[0])
#     minimal_num= names[0]
#     for nume in names:
#         if len(nume)<manimum:
#             manimum=len(nume)
#             minimal_num= nume
#     return minimal_num
# print(check_minimal("e","shaxzod", "jasur","jas"))

# def reversed_words(word):
#     return word[::-1]
# word_=input('Enter a word: ')
# print(reversed_words(word_))



# def reversed_words(*words):
#     reversed_words = []
#     for i, word in enumerate(words):
#         reversed_words.append(word[::-1])
#     return reversed_words
#
# print(reversed_words("word_", "poxxuy"))






# def reverse_recursive(name):
#
#     if len(name) == 0:
#         return name
#     return reverse_recursive(name[1:]) + name[0]
# name = input("Ismingizni kiriting?\n>>>")
# print(f"{name} ismining teskarisi = {reverse_recursive(name)} ga teng:!")





