string=input()
c1=0
for i in range (len(string)):
    x=str(string[i])
    if (x==')'):
        if(c1>=1):
            c1-=1
        else:
            c1=-1
            break
    if(x=='('):
        c1+=1
if c1==0:
    print("yes")
else:
    print("no")
