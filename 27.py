def find_d(lst):
    if (lst[1]-lst[0]) == (lst[2]-lst[1]):
        return "AP",(lst[1]-lst[0])
    elif (lst[1]/lst[0]) == (lst[2]/lst[1]):
        return "GP",(lst[1]/lst[0])
        
def find_terms(lst):
    types,d = find_d(lst)
    lenlst = len(lst)
    if types == "AP":
        for i in range(1,4):
            lst.append((lst[0] + (((lenlst+i)-1)*d)))
    elif types == "GP":
        for i in range(1,4):
            lst.append((lst[0]*(d**(lenlst+i-1))))
    return lst


lst = [2, 6, 18, 54]
lst = find_terms(lst)
print(lst)
