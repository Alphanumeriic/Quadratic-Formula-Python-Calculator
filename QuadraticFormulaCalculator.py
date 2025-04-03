print("Quadratic Formula Calc: Created by Ysf")
print(" ")

print("For complex quadratics j is the same term as i")
print(" ")

import cmath
import math

a = input("What is the a term: ")
b = input("What is the b term: ")
c = input("What is the c term: ")

a = float(a)
b = float(b)
c = float(c)

Calc = (b**2 - 4*a*c)

if Calc > 0:
 Sqrt = math.sqrt(Calc)
else:
  if Calc < 0:
    Sqrt = cmath.sqrt(Calc)


x1 = ((-b + Sqrt)/(a*2))
x2 = ((-b - Sqrt)/(a*2))

print(f"X = {x1}")
print(f"X = {x2}")
