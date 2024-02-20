st = input("Enter String:")

for i in range(len(st)):
    if st[i]=="#":
        n = st[i+1]
        char = st[i+2]
        st = st[:i]+(int(n)*char)+st[i+3:]

print(st)