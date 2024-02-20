#1
# d = {0: 40, 1: 20, 2: 30}
# d = {i[0]:i[1] for i in sorted(d.items(),key=lambda x:x[1])}
# print(d)

#2
# d = {0:1,1:2}
# d[2] = ""
# print(d)

#3
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

#4
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# val = 9
# if val in d.keys():
#     print('present')
# else:
#     print('absent')

#6
# d = {x:x*x for x in range(1,int(input("Enter n:"))+1)}
# print(d)

#13
# keys = ['red', 'green', 'blue']
# values = ['#FF0000', '#008000', '#0000FF']
# d = {x:y for x,y in zip(keys,values)}
# print(d)


#19
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for x,y in d2.items():
#     if x in d1:
#         d1[x] = d1[x]+y
#     else:
#         d1[x] = y
# print(d1)

#24
# s = 'w3resource'
# d = {x:s.count(x) for x in s}
# print(d)

#29
# d = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# d = {x.replace(" ",''):y for x,y in d.items()}
# print(d)

#30
# d = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# d = {i[0]:i[1] for i in sorted(d.items(),key=lambda x:x[1], reverse = True)}
# for x,y in d.items():
#     print('{}   {}'.format(x,y))

#39
# d = {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

# import json

# with open('39dictionary_json','w') as f:
#     json.dump(d,f,indent=4)
    
# with open('39dictionary_json','r') as f:
#     print(f.read())

# #42
# d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# d = {x[0]:x[1] for x in d.items() if x[1]>170}
# print(d)

#47
# d = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# lst = []
# for x in d:
#     for i,y in x.items():
#         if i=='Science':
#             lst.append(y)
# print(lst)

#52
# d = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# vals = set(d.values())
# dct = {}
# for i in vals:
#     dct[i] = list(d.values()).count(i)
# print(dct)

#54
# dic = {'a': 1, 'b': {'c': {'d': {}}}}
# c = 0

# def depth(dic,c):
#     for x,y in dic.items():
#         if type(y) is dict:
#             c += 1
#             c = depth(y,c)
#     return c

# print(depth(dic,c))


#56
# d = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# d = [[x[0],x[1]] for x in d.items()]
# print(d)


#57
# d = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for x,y in d.items():
#     d[x] = [i for i in y if i%2==0]
# print(d)


#63
# d = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# d = {x[0]:[x[1:]] for x in d}
# print(d)


#69
# import math
# d = [7, 23, 3.2, 3.3, 8.4]
# d = {math.floor(x):[i for i in d if math.floor(i)==math.floor(x)] for x in d}
# print(d)

# l = ['Red', 'Green', 'Black', 'White', 'Pink'] 
# l = {len(x):[i for i in l if len(i)==len(x)] for x in l}
# print(l)

#70
# n = [1,2,3,4,5,6]
# x = dict(zip(n,map(lambda i:i*i,n)))  zip used to iterate over n, map used to apply function to all iterables in n
# print(x)

#