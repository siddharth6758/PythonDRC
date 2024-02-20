def count(a,b):
    c = carry = 0
    lsta = [int(x) for x in str(a)]
    lstb = [int(x) for x in str(b)]
    if len(lsta)<len(lstb):
        while len(lsta)!=len(lstb):
            lsta.insert(0,0)
    elif len(lstb)<len(lsta):
        while len(lsta) !=len(lstb):
            lstb.insert(0,0)
    lsta = lsta[::-1]
    lstb = lstb[::-1]
    for x,y in zip(lsta,lstb):
        carry = 1 if x+y+carry>=10 else 0
        if x+y+carry>=10:
            c += 1
        print(x,'+',y,'+',carry,'->',c)
    return c

ct = count(9999,999)
print(ct)
