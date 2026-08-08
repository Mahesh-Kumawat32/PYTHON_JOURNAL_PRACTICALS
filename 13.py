def count_digit(n):
    num = str(n)
    if num.isdigit():
        digits = len(num)
        print(f"Lenght of number {n} is {digits}")

def sum_of_digits(n):
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    print(total)
        
try:
    n = int(input("Enter number : "))
    count_digit(n)
    sum_of_digits(n)
except ValueError:
   print("You enter a wrong number")

