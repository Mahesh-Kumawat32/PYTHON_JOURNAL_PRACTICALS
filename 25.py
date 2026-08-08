#ZeroDivisionError
try:
    n = int(input("ENTER A NUMBER : "))
    print(100/n)

except ZeroDivisionError:
    print("ZeroDivisionError Occurs")

finally:
    print("PROGRAM ENDED!\n")

#ValueError
try:
    n = int(input("ENTER NUMBER : "))
    print(f"NUMBER IS {n}")

except ValueError:
    print("SOMETHING WRONG! PLEASE ENTER A VALID INTEGER")

finally:
    print("PROGRAM ENDED!")