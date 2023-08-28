#Function to detect use of card after check valid or not
def detect_use(Card):
    if(int(str(Card)[0])==4):
        print("Visa card number")
    elif int(str(Card)[0])== 3 and (int(str(Card)[1])== 7 or int(str(Card)[1])==4):
        print("American Express")
    elif int(str(Card)[0])== 5 and (int(str(Card)[1])== 1 or int(str(Card)[1])==2 or int(str(Card)[1])==3 or int(str(Card)[1])==4 or int(str(Card)[1])==5):
        print("MasterCard")
    else:
        print("Invalid")

#Function to check validity using Luhn’s algorithm
def luhn(Card):
    list=[];sum=0;digit=''
    for i in range(len(Card)-2,-1,-2):
        list.append(int(str(Card)[i])*2)
    # print(list)
    for i in range(len(Card)-1,-1,-2):
        sum+=int(str(Card)[i])
    # print(sum)
    for i in range (0,len(list)):
        for digit in str(int(list[i])): 
            sum +=int(digit) 
            # print(int(digit) )
    # print(sum)
    if(sum%10==0):
        return True
    
#main
Card_num=input("Enter Credit number: ")
# print(len(Card_num))
if(luhn(Card_num)):
    detect_use(Card_num)
else:
    print("Invalid")
