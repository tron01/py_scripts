#Count the number of characters (character frequency) in a string. 

st=input("Enter a word:")

c=0
for i in st:
    if i ==" ":
        continue
    else:
        c=c+1
print(c,"character in "+ st)        

