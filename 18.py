t = ()
t = list(t)

for i in range(1,6):
    n = int(input("Enter number : "))
    t.append(n)
count_of_num = int(input("Enter num which total occurance you want to check : "))

#FIND MAXIMUM AND MINUMUM FROM TUPLE
t.sort()
print(f"Maximum : {t[len(t)-1]}")
print(f"Minimum : {t[0]}")
print(f"{count_of_num} is occurs {t.count(count_of_num)} time")

t = tuple(t)
print(f"Tuple is {t}")