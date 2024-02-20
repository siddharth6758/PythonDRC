n = int(input("Enter number > 4:"))

lst = []

for i in range(2,n):
    flag = 0
    for x in range(2,i):
        if i%x==0:
            flag = 1
            break
    if flag==0:
        lst.append(i)

for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i] + lst[j] == n:
            print(lst[i],'+',lst[j])