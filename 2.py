import random as rn

lst = []
vowels = ['a','e','i','o','u']
count = 0
while True:
    rn.shuffle(vowels)
    ch = "".join(vowels)
    if ch not in lst:
        lst.append(ch)
        count += 1
    if count == 120:
        break
    
print(lst)
