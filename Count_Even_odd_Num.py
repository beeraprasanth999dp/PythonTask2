#Even Numbers from m to n
m = 3
n = 7
even_count = 0
odd_count = 0

for i in range(m, n + 1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even =", even_count, ", Odd =", odd_count)



