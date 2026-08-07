n = int(input("Enter a number : "))
#prints even numbers
print("even")
for i in range(0,n+1):
    if i%2==0:
        print(i,end=",")
    else:
        continue
#prints odd numbers
print("\nodd")
for j in range(0,n+1):
    if j%2!=0:
        print(j,end=",")
    else:
        continue