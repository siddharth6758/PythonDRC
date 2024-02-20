# n = int(input("Enter number:"))
n = 6
for i in range(n):
	for j in range(n):
		if i+j>=n-1:
			print(" 0",end="")
		else:
			print(" ",end="")
	print()

# for i in range(n):
#     for j in range(n):
#         if i+j==n-1 or i==n-1 or j==n-1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     # for j in range(n):
#     #     if i==j:
#     #         print('*',end='')
#     #     elif i==n-1:
#     #         print('*',end='')
#     #     else:
#     #         print(' ',end='')
#     print()    