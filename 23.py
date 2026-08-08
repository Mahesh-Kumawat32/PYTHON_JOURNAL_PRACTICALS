#WRITE DATA INTO FILE data.txt
with open('data.txt',"w") as f:
    f.write("Hello! This is a file handling code")

with open('data.txt',"r") as f:
    print(f.read())