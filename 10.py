def find_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(f"Factorial of {n} is {fact}")

n = int(input("Enter number which factorial you want : "))
find_factorial(n)