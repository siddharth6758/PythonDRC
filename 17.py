# def strobogrammatic(n,digits=[]):
#     result = []
#     if n==0:
#         print('in 0')
#         return result
#     if n==1:
#         print('in 1')
#         result.extend([0,1,8])
#         return result
#     if n>=2:
#         print('in 2')
#         for i in digits:
#             result.append(int('1'+str(i)+'1'))
#             result.append(int('6'+str(i)+'9'))
#             result.append(int('8'+str(i)+'8'))
#             result.append(int('9'+str(i)+'6'))
#         n = n - 1
#         result = strobogrammatic(n,result)
#     return result
    
    
def strobogrammatic(n,result=[]):
    if n==0:
        print('in 0')
        return result
    if n==1:
        print('in 1')
        result.extend([0,1,8])
        return result
    if n>=2:
        print('in 2')
        for i in range(n):
            result = strobogrammatic(i,result)
            print(i,":",result)
            for i in result:
                print(i)
                result.append(int('1'+str(i)+'1'))
                result.append(int('6'+str(i)+'9'))
                result.append(int('8'+str(i)+'8'))
                result.append(int('9'+str(i)+'6'))
    return result

n = int(input("Enter no. of digits: "))
res = strobogrammatic(n)
print(res)
