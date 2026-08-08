import math

n = int(input("Enter a number : "))
print(f"The square root of {n} is {math.sqrt(n)}")

base = int(input('Enter base : '))
exponent = int(input("Enter power : "))
print(f"The Value of {base}^{exponent} is {math.pow(base,exponent)}")

radius = float(input("Enter radius of circle : "))
print(f"The Area of cirlce is {round(math.pi*radius**2)}")