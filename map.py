# i = [1,2,3,4,5]
# print(list(map(lambda x:x*3,i)))

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# nums3 = [7, 8, 9]
# print(list(map(lambda x,y,z:x+y+z,nums1,nums2,nums3)))

# l = ['Red', 'Blue', 'Black', 'White', 'Pink']
# print(list(map(lambda x:[i for i in x],l)))

# i = [1,2,3,4,5]
# print(list(map(lambda x,y:x**y,i,[x for x in range(len(i))])))

# a = [3,4,5,6,7,8,9]
# b = [1,2,3,4,5,6,7]
# print(list(map(lambda x,y:(x+y,x-y),a,b)))

# nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
# nums2 = [2, 2, 3, 1, 2, 6, 7, 9]
# def count(a,b):
#     c = 0
#     if a==b:
#         c += 1
#     return c
# print(sum(list(map(count,nums1,nums2))))

# a = [3,4,5,6]
# b = [1,2,3,4]

# nlst = []
# def interleave(a,b):
#     nlst.append(a)
#     nlst.append(b)
#     return nlst

# nlst = list(map(interleave,a,b))
# print(nlst)

