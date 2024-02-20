def permut(n):
    ct = 0
    digits = [x for x in range(10)]
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if a+b+c+d==n:
                        ct += 1
    return ct
                    
n = int(input("Enter number:"))
ct = permut(n)
print(ct)