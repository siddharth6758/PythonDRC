import re

def slope(ln):
    c1,c2 = ln
    return (c2[1]-c1[1])/(c2[0]-c1[0])

def isParallel(ln1,ln2):
    s1 = slope(ln1)
    s2 = slope(ln2)
    print(s1,':',s2)
    if (s1) == (s2):
        return True
    return False
    
    
ptn = r','
ln1 = []
for i in range(2):
    ln = input(f"Enter x{i+1},y{i+1}:")
    ln1.append(tuple(int(x) for x in re.split(ptn,ln) if x.isdigit()))
ln2 = []
for i in range(2):
    ln = input(f"Enter x{i+3},y{i+3}:")
    ln2.append(tuple(int(x) for x in re.split(ptn,ln) if x.isdigit()))

res = isParallel(ln1,ln2)
print("Is Parallel : ",res)