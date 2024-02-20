class Zip:
    def __init__(self,val1,val2):
        self.l1 = val1
        self.l2 = val2
        self.st = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if len(self.l1)!=len(self.l2):
            raise Exception("Length not Equal Error")
        else:
            if self.st == len(self.l1):
                raise StopIteration
            else:
                x,y = self.l1[self.st],self.l2[self.st]
                self.st += 1
                return (x,y)
    
l1 = [1,2,3,4,5]
l2 = [5,4,3,2,1]
# f = Zip([1,2,3,4],[5,6,7,8])
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

for i in Zip(l1,l2):
    print(i)