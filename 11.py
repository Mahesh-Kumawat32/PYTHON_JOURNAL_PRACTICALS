n =  int(input('Enter range of fibonacci series : '))
def find_fib(n):
    a,b = 0,1
    for i in range(0,n+1):
        print(a, end= " ")
        c = a+b
        a = b
        b = c
find_fib(n)