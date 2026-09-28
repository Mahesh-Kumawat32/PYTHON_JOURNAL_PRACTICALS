a = int(input("ENTER FIRST NUM : "))
b = int(input("ENTER SECOND NUM : "))
c = int(input("ENTER THIRD NUM : "))

if a>b and a>c:
    print(f"{a} IS GREATER")
elif b>a and b>c:
    print(f"{b} IS GREATER")
else:
    print(f"{c} IS GREATER")

