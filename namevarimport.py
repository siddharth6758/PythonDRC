class Calc:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def mul(self):
        return self.a * self.b
    
    def sub(self):
        return self.a - self.b
    
    def div(self):
        return self.a / self.b
    
    def mod(self):
        return self.a % self.b
    
    
print("Calc __name__: ",__name__)
if __name__ == "__main__":
    print("Direct Calc")
else:
    print("Imported Calc")