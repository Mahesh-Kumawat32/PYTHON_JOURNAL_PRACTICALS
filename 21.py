something = input("Enter some Words : ")
l = something.split()

#WORDS IN STRING
print(f"TOTAL WORDS : {len(l)}")

#CHARACTERS IN STRING
something = list(something)
print(f"TOTAL CHARACTERS : {len(something)}")

#VOWELS IN STRING
cnt = 0
for i in range(0,len(something)):
    if (something[i].upper() =='A' or
        something[i].upper() =='U' or
        something[i].upper() =='I' or
        something[i].upper() =='O' or
        something[i].upper() =='E' ):
        cnt = cnt + 1
    else:
        continue
print(f"TOTAL VOWELS : {cnt}")



