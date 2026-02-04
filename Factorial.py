#factorial of number
n=6
fact=1
if(n==0 or n==1):
    print("1")
else:
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
def fat(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n=5
print()
