#perfect Number or not
num=28
sum_div=0
for i in range(1,num):
    if num %i==0:
        sum_div+=i
if sum_div==num:
    print("perfect number")
else:
    print("not perfect number")