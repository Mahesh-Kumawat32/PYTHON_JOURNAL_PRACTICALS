import random
num = []
for i in range(1,11):
    n = random.randint(1,100)
    num.append(n)
print(num)
num.sort()
print(num[len(num)-1])
