print("BEFORE TYPE CONVERSION")

a = 19
b = 12.55
c = "Something"

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))
print("-"*30)
print("AFTER TYPE CONVERSION")

a = float(a)
b = int(b)
print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))