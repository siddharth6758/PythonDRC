class OperatorOverloader:
    
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
        
    def __mul__(self,other):
        print("This is Exponential: ",end='')
        return int(self.val1)**int(other.val2)
    
    def __add__(self,other):
        print("This is Concatenate: ",end='')
        return str(self.val1)+str(other.val2)
    
    def __repr__(self):
        return "val1: {} & val2: {}".format(self.val1,self.val2)
    
    def __format__(self):
        return "This is val1: {} \nThis is val2: {}".format(self.val1,self.val2)
    
ol = OperatorOverloader(10,2)
ot = OperatorOverloader(30,40)
print(ol+ot)
print(ol)
print(ol*ot)
print(ot.__format__())
print(ol.__sizeof__())

# class ABC:
#     pass

# a = ABC()
# print(a.__sizeof__())