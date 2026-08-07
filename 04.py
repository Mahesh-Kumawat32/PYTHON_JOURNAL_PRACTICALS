choice = int(input("1.FIND RECTANGE AREA\n2.FIND CIRCLE AREA\nENTER NUMBER WHOSE AREA YOU WANT TO FIND : "))
match choice :
    case 1:
        length = float(input("LENGHT OF RECTANGLE : "))
        width = float(input("WIDTH OF RECTANGLE : "))
        print(f"AREA OF RECTANGEL IS : {length*width}")
    case 2:
        radius = float(input("ENTER RADIUS OF CIRCLE : "))
        print(f"AREA OF CIRCLE IS : {round(3.14*radius*radius)}")
    case _:
        print("YOU ENTER SOMETHING WRONG !")