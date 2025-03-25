# from src.main import func, Logic
#
# def test():
#     assert 1==1
#
#
#
# def test_func():
#     assert func(4)==5
#     assert func(9)==10
#
#
# def test_logic():
#     assert Logic.logic_param==10


#
# import pytest
# from src.main import sum_ as _sum
#
#
#
# def test_func():
#     x=1
#     y=2
#     result =3
#     assert _sum(x,y)==result
#
#
# def test_sum_type_failure():
#     x=1
#     y='2'
#     pytest.raises(TypeError, _sum, x, y)
#
#
#
#
# def test_sum_value_failure():
#     x=1
#     y=2
#     result =4
#     assert _sum(x,y)!=result
#
#
#
#
# def test_sum_negative():
#     x = -5
#     y = -5
#     result = -10
#     assert _sum(x, y) == result
#
#
#
#
# def test_sum_zero():
#     x = 0
#     y = 0
#     result = 0
#     assert _sum(x, y) == result
#
#
#
# def test_big_numbers():
#     x = 2**10
#     y = 100
#     result=2**10+100
#     assert _sum(x, y) == result
#
#
#
# def test_sum_float():
#     pytest.raises(TypeError, _sum, 1.0, 2.0)
#
#
# def test_sum_list():
#     pytest.raises(TypeError, _sum, [1, 2], [3, 4])
#
#
# def test_sum_dict():
#     pytest.raises(TypeError, _sum, {'a': 1}, {'b': 2})
#
# def test_sum_complex():
#     pytest.raises(TypeError, _sum, 1+2j, 2+3j)


# from contextlib import nullcontext as does_not_raise
# from src.main import sum_
# import pytest
#
# @pytest.mark.parametrize(
#     "x, y, expected, expectation",
#     [
#         (1, 2, 3, does_not_raise()),
#         (-1, -1, -2, does_not_raise()),
#         (2**10, 100, 2**10+100, does_not_raise()),
#         (1, "1", 2, pytest.raises(TypeError)),
#         (1.0, 2.0, 3.0, pytest.raises(TypeError)),
#         ([1, 2], [3, 4], [1,2,3], pytest.raises(TypeError)),
#         ({'a': 1}, {'b': 2}, {}, pytest.raises(TypeError)),
#         (1+2j, 2+3j, 5+6j, pytest.raises(TypeError)),
#     ]
# )
# def test_sum_success(x, y, expected, expectation):
#     with expectation:
#         assert sum_(x, y) == expected


import pytest

# def findClosestNumber(self, nums):
#     evens = list(map(abs, nums))
#
#     closest = min(evens)
#     closest_negative = closest * -1
#     if closest in nums:
#         return closest
#     return closest_negative


#
# @pytest.mark.parametrize(
#     'numbers, expected',
#     [
#         ('[1,2,3]',TypeError),
#         (5j,TypeError),
#         (['a','b','c'],TypeError),
#     ]
# )
# def test_findClosestNumber(numbers, expected):
#     pytest.raises(expected, findClosestNumber, numbers)


def isAnagram(s, t):
    if not isinstance(s, str) or not isinstance(t, str):
        raise TypeError("Arguments must be strings")
    if len(s) != len(t):
        return False

    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True


# def isAnagram(s, t):
#     if not isinstance(s, str) or not isinstance(t, str):
#         raise TypeError('Arguments must be strings')
#     if len(s) != len(t):
#         return False
#
#     for i in set(s):
#         if s.count(i) != t.count(i):
#             return False
#     return True
#
#
#
# import pytest
# from contextlib import nullcontext as does_not_raise
#
# @pytest.mark.parametrize(
#     "s, t, expected, x",
#     [
#         ("anagram", "nagaram", True, does_not_raise()),
#         ("rat", "tar", True, does_not_raise()),
#         ("hello", "world", False, does_not_raise()),
#         ("", "", True, does_not_raise()),
#
#         (["anagram"], "nagaram", True, pytest.raises(TypeError)),
#         ("hello", 123, False, pytest.raises(TypeError)),
#         (None, "world", False, pytest.raises(TypeError)),
#         (1234, 5678, False, pytest.raises(TypeError))
#     ]
# )
# def test_isAnagram(s, t, expected, x):
#     with x:
#         assert isAnagram(s, t) == expected


# def test_fixture(example_fixture):
#     name= example_fixture["name"]
#     assert name == "Alex"


@pytest.mark.parametrize(
    "s, t, expected, x",
    [
        ("anagram", "nagaram", True, does_not_raise()),
        ("rat", "tar", True, does_not_raise()),
        ("hello", "world", False, does_not_raise()),
        ("", "", True, does_not_raise()),
        (["anagram"], "nagaram", True, pytest.raises(TypeError)),
        ("hello", 123, False, pytest.raises(TypeError)),
        (None, "world", False, pytest.raises(TypeError)),
        (1234, 5678, False, pytest.raises(TypeError)),
    ],
)
def test_isAnagram(s, t, expected, x):
    with x:
        assert isAnagram(s, t) == expected
