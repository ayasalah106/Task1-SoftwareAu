# arr=['a','x','n','b']
# arr.sort()
# print(arr)
def check(st1,st2):
    if len(st1)!=len(st2):
        return False
    for i in range (len(st1)):
        if(st1[i]!=st2[i]):
            return False
    return True    

arr=[]
for i in range(2):
    x=input(f"Enter string {i+1}: ")
    arr.append(sorted(x))
if check(arr[0],arr[1]):
    print("yes,they are anagrams")
else:
    print("NOO")