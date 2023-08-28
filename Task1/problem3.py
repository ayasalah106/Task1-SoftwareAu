Bills = [200, 100, 50, 20, 10, 5, 1]

def Calculate(amount):
  final = []
  for x in Bills:
    if amount >= x:
    #floor division 
      count = int(amount/x)
      final.append(f"{count} x {x}  L.E.")
      amount %= x
    #join would combine into string
  return " + ".join(final)

amount = int(input("Enter amount in Egyptian Pounds: "))
print(Calculate(amount))












# def calculate(num):
#     counter_1=counter_5=counter_10=counter_20=counter_50=counter_100=counter_200=0
#     while(num-200>=0):
#         (counter_200)+=1
#         num=num-200
#     while(num-100>=0):
#         (counter_100)+=1
#         num=num-100
#     while(num-50>=0):
#         (counter_50)+=1
#         num=num-50
#     while(num-20>=0):
#         (counter_20)+=1
#         num=num-20
#     while(num-10>=0):
#         (counter_10)+=1
#         num=num-10
#     while(num-5>=0):
#         (counter_5)+=1
#         num=num-5
#     while(num-1>=0):
#         (counter_1)+=1
#         num=num-1
# print(calculate(300))