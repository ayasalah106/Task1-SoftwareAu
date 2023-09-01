def sum(arr,start,end,target):
    if start ==end :
        return -1,-1
    if(arr[start]+arr[end]==target):
        return arr[start] , arr[end]
    elif(arr[start]+arr[end]<target):
        return sum(arr,start+1,end,target)
    elif(arr[start]+arr[end]>target):
        return sum(arr,start,end-1,target)


n=int(input("Enter size of array: "))
arr=[]
for i in range(n):
    arr.append(int(input()))
target=int(input("Enter target: "))
arr.sort()
x,y =sum(arr,0,n-1,target)
if(x==-1):
    print("No")
else:
    print(f" yes,{target} = {x} + {y}")
