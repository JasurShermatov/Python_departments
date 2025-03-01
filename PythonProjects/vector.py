import math

"""Bu yerda Vector nomli class da ikki vectorni qo'shish orqali yoki ayirish orqali 3-vectorni topishni yoki 
ikki vectorni bir biriga taqqosslashni uchun dastur yozganmiz"""


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector: <{self.x}, {self.y}>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __lt__(self, other: "Vector"):
        return self.magnitude < other.magnitude

    def __gt__(self, other):
        return self.magnitude > other.magnitude

    @property
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


""" v3 = v1 + v2 #Bu yerda v1 va v2 ni yig'indisi orqali v3 topilgan """
v1 = Vector(6, 7)
""" v3 = v1 - v2 #Bu yerda v1 va v2 ni ayirish  orqali v3 topilgan """
v2 = Vector(3, 3)
# print(v3)

if v1 > v2:
    print("v1 is longer")
    """Bu yerda 2 ta Vector solishtirilgan """
else:
    print("v2 is longer")