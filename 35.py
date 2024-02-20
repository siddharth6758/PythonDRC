import re

ptn = r'[x+y=]'

eq1 = input("Enter equation1 (ax+by=c):")
eq2 = input("Enter equation2 (dx+ey=f):")

a,b,c = [int(x) for x in re.split(ptn,eq1) if x.isdigit()]
d,e,f = [int(x) for x in re.split(ptn,eq2) if x.isdigit()]

A = ((a*e)-(b*d))
A1 = ((c*e)-(b*f))
A2 = ((a*f)-(c*d))

x = A1/A
y = A2/A

print(x,":",y)
