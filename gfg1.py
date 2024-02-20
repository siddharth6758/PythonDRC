a = "abcdefg"
b = "qpabcdjk"
c = ""

def func(a,b,c):
    maxlen = 0
    st = ""
    if len(a)<=len(b):
        obs = a if len(a)<=len(c) else c
    else:
        obs = b if len(b)<=len(c) else c
    count = 0
    for i in obs:
        st += i
        if (a.find(st) != -1) and (b.find(st) != -1) and (c.find(st) != -1):
            count+=1
            if maxlen<count:
                maxlen = count
        else:
            st = ""
            count = 0
        
    return maxlen
    
maxlen = func(a,b,c)
print(maxlen)
