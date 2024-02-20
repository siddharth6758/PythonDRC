def absdif(lst):
    dif = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            dif += abs(lst[i] - lst[j])
    return dif
        
lst = [1,2,3]
diff = absdif(lst)
print(diff)
