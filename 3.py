lst = [1,2,3,4,5,6,7,8,9,0]

while len(lst)>=0:
    print(lst)
    if len(lst)<=2 and len(lst)>0:
        lst.pop()
    elif len(lst) == 0:
        break
    else:
        lst.pop(2)
