while True:  
    num = int(input("ENTER A NUMBER : "))
    if num>0:
        print("NUM YOU ENTER IS POSITIVE")
        break
    elif num==0:
        print("NUM YOU ENTER IS ZERO")
        break
    elif num<0:
        print("NUM YOU ENTER IS NEGATIVE")
        break
    else:
        print("INVALID INPUT")
        continue
if num%2==0:
    print("NUM IS EVEN")    
else:
    print("NUM IS ODD")

