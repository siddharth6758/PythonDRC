class Dupli:
    def __init__(self,val):
        self.lst = val
        self.start = 0
        self.nlst = []
    
    # def __iter__(self):
    #     return self
    
    def __next__(self):
        if self.lst[self.start] not in self.nlst:
            self.nlst.append(self.lst[self.start])
            self.start += 1
        else:
            self.start += 1
        return self.nlst
            
            
f = Dupli([1,1,3,4,2,1,4,5,6,5])
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