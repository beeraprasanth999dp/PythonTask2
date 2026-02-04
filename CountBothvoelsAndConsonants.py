#count Number of Vowels and consonants
str="apple"
count=0
temp=0
for ch in str:
    if ch  in "aeiouAEIOU":
        count+=1
    elif ch.isalpha():
        temp+=1

print("Number of vowels:", count)
print("Number of consonants:",temp)
