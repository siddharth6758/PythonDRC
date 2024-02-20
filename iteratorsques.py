class SumIter:
    def __init__(self,val):
        self.lst = val
        self.start = 0
        self.sums = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.sums += self.lst[self.start]
        self.start += 1
        return self.sums
            
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