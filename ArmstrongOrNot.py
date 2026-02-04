
#Armstrong or not
n=153
org=n
total=0
while n>0:
    digit=n%10
    total += digit**3
    n=n//10
if total==org:
    print("Armstrong")
else:
    print("Not Armstrong")
