#product of digits
n=153
count=1
while n>0:
    digit=n%10
    count=count*digit
    n//=10
print(count)
