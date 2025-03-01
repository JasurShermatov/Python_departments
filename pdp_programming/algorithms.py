# def clothest_zero(list_):
#     return min(list_, key=lambda x: abs(x))
#
# numbers=[-5, 5, 10, -10,2, 3, 4, 5, 6, 7, 8, 9, 10,1, -1]
# print(clothest_zero(numbers))




# class Solution(object):
#     def findClosestNumber(self, nums):
#         evens = list(map(abs, nums))
#
#         closest = min(evens)
#         closest_negative = closest * -1
#         if closest in nums:
#             return closest
#         return closest_negative




# def has_duplicate(list_):
#     return len(list_) != len(set(list_))
# print(has_duplicate([1, 2, 3, 4]))
# print(has_duplicate([1, 2, 3, 1]))




# class Solution:
#     def isHappy(self, n: int) -> bool:
#         seen = set()
#         while n != 1 and n not in seen:
#             seen.add(n)
#             n = sum(int(digit) ** 2 for digit in str(n))
#         return n == 1





# def fiz_biz(n):
#     result = []
#     for i in range(1, n + 1):
#         if i % 15 == 0:
#             result.append("fiz biz")
#         elif i % 3 == 0:
#             result.append("fiz")
#         elif i % 5 == 0:
#             result.append("biz")
#         else:
#             result.append(str(i))
#     return ", ".join(result)
#
# n = int(input("Son kiriting: "))
# print(fiz_biz(n))
#



def  check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(check_anagram("listenk", "silent"))





