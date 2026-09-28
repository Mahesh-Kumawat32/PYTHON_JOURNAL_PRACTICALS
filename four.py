    
while True:
    print("1. AREA OF RECTANGLE")
    print("2. AREA OF CIRCLE")
    choice = int(input('ENTER YOUR CHOICE : '))
    match choice : 
        case 1 :
            length  = float(input("LENGTH OF RECTANGLE : "))
            width = float(input("WIDTH OF RECTANGLE : "))
            print(f"AREA OF RECTANGLE IS {length* width}")
            break
        case 2:
            r = float(input("RADIUS OF CIRCLE : "))
            print(f"AREA OF CIRCLE IS {3.14*r*r}")
            break
        case _:
            print("INVALID CHOICE!")
            continue
        