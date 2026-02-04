#Check Neon number
num=9
sq=num*num
temp=0
while sq>0:
    temp+=sq%10
    sq //=10
if temp==num:
    print("Neon Number")
else:
    print('not neon number')