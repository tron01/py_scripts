y=int(input("Enter the year"))
b=int(2022)
for i in range(b,y):
    if i%4==0 and i%100!=0:
        print(i)