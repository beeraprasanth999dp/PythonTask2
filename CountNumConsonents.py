#Count Consonants
str="prasanth"
count=0
for ch in str:
    if ch not in "aeiouAEIOU":
        count+=1
print("Number of cononants:",count)