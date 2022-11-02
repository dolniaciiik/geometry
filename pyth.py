import math

def calc_c(a,b):
    c = math.sqrt(a**2+b**2)
    return c

print(calc_c(int(input("a:")), int(input("b:"))))
