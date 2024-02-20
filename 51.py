n = [int(x) for x in input("Enter 8 digit number:")]
sn = int(''.join([str(x) for x in sorted(n)]))
ln = int(str(sn)[::-1])
print(ln-sn)