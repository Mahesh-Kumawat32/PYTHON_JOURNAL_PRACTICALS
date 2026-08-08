#COUNT THE LINES OF FILE data.txt
with open('data.txt',"r") as f:
    cnt = 0
    while True:
        line = f.readline()
        if line!="":
            cnt = cnt+1
        else:
            break
    print(f"TOTAL LINES IN FILE : {cnt}")

#COUNT TOTAL WORDS & CHARACTERS IN FILE data.txt
with open('data.txt',"r") as f:
    data = f.read()
    l = data.split()
    characters = list(data)
    print(f"TOTAL WORDS IN FILE : {len(l)}")
    print(f"TOTAL CHARACTERS : {len(characters)}")




