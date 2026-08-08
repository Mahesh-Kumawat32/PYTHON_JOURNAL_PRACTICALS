something = input("Enter something : ").upper()

print(f"ORIGINAL CONTENT : {something}")
print(f"REVERSED CONTENT : {something[::-1]}")

#CHECK THAT STRING IS PALINDROME OR NOT
if something==something[::-1]:
    print(f"STRING IS PALINDROME")
else:
    print(f"STRING IS NOT PALINDROME")