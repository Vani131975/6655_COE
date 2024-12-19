import math

def cal_hypotenuse(a, b):
  return math.sqrt(a**2 + b**2)

a = float(input("Enter a length: "))
b = float(input("Enter b length: "))
hypotenuse = cal_hypotenuse(a, b)
print(f"The hypotenuse of the right angle triangle is: {hypotenuse:.2f}")
