def fibo(n):
	count = 1
	a = 0
	b = 1
	while count<=n:
		yield a
		a,b = b,a+b
		count += 1


f = fibo(10)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
