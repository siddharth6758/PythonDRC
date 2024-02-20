class SumIter:
    def __init__(self,val):
        self.lst = val
        self.start = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        flag = 0
        # print(self.lst[self.start])
        for i in range(2,self.lst[self.start]):
            if self.lst[self.start]%i==0:
                flag = 1
                break
        if flag==0:
            res = self.lst[self.start]
            self.start += 1
            return res
        else:
            self.start += 1
            return ''
            
            
f = SumIter([1,2,3,4,5,6,7,8,9,10])
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))