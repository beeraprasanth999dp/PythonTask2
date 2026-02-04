#Sum of digits
n=123
count=0
while n>0:
    digit=n%10
    count=count+digit
    n//=10
print(count)
