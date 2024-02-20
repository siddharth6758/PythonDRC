from namevarimport import Calc

# class Calc:
    
#     def __init__(self,a,b):
        # print("Here")
#         self.a = a
#         self.b = b
    
#     def add(self):
#         return self.a + self.b
    
#     def mul(self):
#         return self.a * self.b
    
#     def sub(self):
#         return self.a - self.b
    
#     def div(self):
#         return self.a / self.b
    
#     def mod(self):
#         return self.a % self.b


print("Namevar.py __name__: ",__name__)

cal = Calc(10,20)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
print(cal.mod())


if __name__ == "__main__":
    print("Direct Name_var")
else:
    print("Imported Name_var")