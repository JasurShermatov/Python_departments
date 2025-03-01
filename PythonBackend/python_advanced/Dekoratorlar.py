# from operator import sub
#
#
# def calculate(func, a, b):
#     return func(a, b)
#
#
# res = calculate(sub, 1, 4)
# print(res)


# def func():
#     def another_func():
#         return 1
#     return another_func()
#
#
# another = func()
# print(another)


# import time
#
#
# def timer(func):
#     def inner():
#         started = time.time()
#         func()
#         finished = time.time()
#         print(f"Took {finished - started} seconds")
#     return inner
#
#
# @timer
# def do1():
#     time.sleep(3)
#     print("Do1 is done")
#
#
# @timer
# def do2():
#     time.sleep(2)
#     print("Do2 is done")
#
#
# do1()
# do2()

#
# def star(func):
#     def inner():
#         print("*"*12)
#         func()
#         print("*"*12)
#     return inner
#
# def percent(func):
#     def inner():
#         print("%"*12)
#         func()
#         print("%"*12)
#     return inner
#
# @percent
# @star
# def hello():
#     print("Hello world")
#
#
# hello = star(hello)
# hello()






# import datetime
import time
# def log(func):
#     def inner():
#         start=datetime.datetime.now()
#         print (f"\n - called function: {func.__name__} at {start.strftime('%H:%M:%S')}\n")
#         func()
#         end=datetime.datetime.now()
#         print(f"\n - finished function: {func.__name__} at {end.strftime('%H:%M:%S')}\n")
#     return inner
#
# @log
# def hello():
#     print("Hello")
# hello()


# import datetime
# import time
# def log(func):
#     def inner():
#         start=datetime.datetime.now()
#         print (f"\n - called function: {func.__name__} at {start.strftime('%H:%M:%S')}\n")
#         func()
#         end=datetime.datetime.now()
#         print(f"\n - finished function: {func.__name__} at {end.strftime('%H:%M:%S')}\n")
#     return inner
#
# @log
# def hello():
#     print("Hello")
# hello()


import time


import time
from contextlib import contextmanager


@contextmanager
def log():
    start_time = time.strftime("%H:%M:%S")
    print(f"- context manager opened at {start_time}")
    try:
        yield
    finally:
        end_time = time.strftime("%H:%M:%S")
        print(f"- context manager closed at {end_time}")


# Usage example
with log():
    print("hello")
