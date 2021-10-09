def fib(high):
	x = 0
	y = 1
	count = 0
	while count < high:
		x, y = y, x + y
		yield x
		count += 1
for n in fib(1000000):
 	# print(n)