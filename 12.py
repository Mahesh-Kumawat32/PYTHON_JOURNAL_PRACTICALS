n = int(input('Enter a number : '))
def prime_or_not(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i==0:
            cnt += 1
    if cnt ==2:
        print (f"{n} is prime")
    else:
        print(f"{n} is not prime")

def palindrome_or_not(n):
    temp = n
    reverse = 0
    remain = 0
    while temp>0:
        remain = temp % 10
        reverse = reverse * 10 + remain
        temp = temp //10
    if reverse == n:
        print(f"{n} is Palindrome")
    else:
        print(f"{n} is not palindrome")

prime_or_not(n)
palindrome_or_not(n)
        