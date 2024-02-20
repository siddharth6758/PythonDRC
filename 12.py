def perm(start, end=[]):
    print('start fn:',start)
    if(len(start) == 0):
        print(end)
    else:
        for i in range(len(start)):
            print(i,": in loop :",start,'->',end)
            perm(start[:i] + start[i+1:], end + start[i:i+1])
            
            
perm([1,2,3,4])

