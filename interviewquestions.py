# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(7))

#==================================================

# def freq_count(lst):
#     freq = {}
#     for i in lst:
#         if i in freq.keys():
#             freq[i] += 1
#         else:
#             freq[i] = 1
#     return freq

# lst = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
# print(freq_count(lst))

#==================================================

# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# print(is_prime(3))


#==================================================

#ways to change replace keys in dictionary
# dct = {"A":1,"B":2,"C":3,"D":4}
# print(dct)

# dct["E"] = dct["B"]
# del dct["B"]
# print(dct)

# dct['E'] = dct.pop('B')
# print(dct)

#==================================================

# coins = [int(x) for x in input('Enter coins with space:').split(' ')]
# coins = sorted(coins)
# amt = int(input("Enter amount: "))
# def solve_coin_change(denominations, amount):
#     solution = [0] * (amount + 1)
#     print(solution)
#     solution[0] = 1
#     print(solution)
#     for den in denominations:
#         for i in range(den, amount + 1):
#             solution[i] += solution[i - den]

#     return solution[len(solution) - 1]

# denominations = [1,2,5]
# amount = 5

# print(solve_coin_change(denominations,amount))



#=========================================================================
# def check_input(func):
#     def inner(n):
#         if n<0:
#             raise ValueError("Less than 0")
#         return func(n)
#     return inner

# @check_input
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)
        
# print(fact(5))

#=============================================================================

# def fibo(n):
#     count = 0
#     a = 0
#     b = 1
#     while count<=n:
#         yield a
#         a,b = b,a+b
#         count += 1
    
# f = fibo(10)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))


#=============================================================================

# class VowelIterator:
    
#     def __init__(self,val):
#         self.lst = list(val)
#         self.start = 0
        
#     def __iter__(self):
#         return self.lst
    
#     def __next__(self):
#         if self.lst[self.start] in 'aeiou':
#             res = self.lst[self.start]
#             self.start += 1
#             return res
#         else:
#             self.start += 1   
#             return ''
            
# f = VowelIterator('abucode')
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

#=============================================================================

# a = 'abcoude'
# VowelIterator = iter(x for x in a if x in 'aeiou')

# x = VowelIterator
# print(next(VowelIterator))
# print(next(x))
# print(next(x))
# print(next(x))