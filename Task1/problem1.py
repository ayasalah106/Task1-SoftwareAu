
#taking input from user with validation
x=1  
i=int(input("Enter number between 1 and 8: "))
while x:
    print(i)
    if 1 <= i <= 8 : 
        x=0
    else:
        i=int(input("Enter again in range please:  "))
#draw
for c in range (1,i+1):
    for r in range (1,i+1-c):
        print(" ",end="")        
    for v in range(0,c):
        print("#",end="")
    print(" ",end="")
    for v in range(0,c):
        print("#",end="")
    print("\n")
        