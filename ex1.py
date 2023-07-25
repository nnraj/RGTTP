"""
  Lesson 1: ex1.py
"""

# 1. Identify type of the each variable below and add as a type hint
#    during the declaration.

# For example:
a: int = 2023

b = 42.5
b: float = 42.5

c = "42"
c: str = "42"

d = "\u0CA0"
d: str = "\u0CA0"

e = "False"
e: str = "False"

f = False
f: bool = False

g = len("updated")
g: int = len("updated")

h = 100**10
h: int = 100**10

i = 2 > 1
i: bool = 2 > 1

j = 30 % 7
j: int = 2

k = 30/7
k: float = 30/7

l = b + 3  # noqa: E741
l: float = b + 3 # 45.5

m = 128 >> 1
m: int = 128 >> 1

n = bin(128)
n: str = bin(128)

o = [m, l, k, n]
o: list = [m, l, k, n]

p = len(o)
p: int = len(o)


