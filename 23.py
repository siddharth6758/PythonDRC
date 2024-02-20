def subs(n,sumd,count=0):
    if n<=0:
        return count
    else:
        count += 1
        return subs(n-sumd,sumd,count)
    
n = int(input("Enter number:"))
sumd = sum([int(x) for x in str(n)])
print(subs(n,sumd))
