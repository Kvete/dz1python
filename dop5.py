"""dop5"""
import math

ax = int(input("give me Ax "))
ay = int(input("give me Ay "))
bx = int(input("give me Bx "))
by = int(input("give me By "))
r = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
print(f'расстояние между точками А и B ={r}')
