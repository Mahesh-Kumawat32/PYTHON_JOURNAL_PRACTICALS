n = int(input("Enter a number : "))
if n>0:
    print(f"{n} is positive")
elif n<0:
    print(f"{n} is negative")
elif n==0:
    print(f"{n} is zero")
else:
    print(f"You enter a wrong number")

temp = abs(n)
if temp%2==0:
    print(f"{temp} is even")
else:
    print(f"{temp} is odd")

    
