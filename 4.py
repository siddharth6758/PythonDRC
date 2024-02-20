x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
# for i in range(len(x)-2):
#     for j in range(i+1,len(x)-1):
#         for k in range(j+1,len(x)):
#             if (x[i] != x[j] != x[k]) and (x[i]+x[j]+x[k] == 0):
#                 print(x[i],":",x[j],":",x[k])
#                 break

for i in range(len(x)-2):
    j = i+1
    k = j+1
    if (x[i] != x[j] != x[k]) and (x[i]+x[j]+x[k] == 0):
        print(x[i],":",x[j],":",x[k])
        break
