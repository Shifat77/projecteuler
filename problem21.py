def sumOfDivisor(num1):
	sum = 0
	for a in range (1, num1):
		if num1 % a == 0:
			sum += a
	return sum


for c in range(1, 10000):
	print(c)
	sum2 = 0
	x = sumOfDivisor(c)
	for d in range(1, c):
		y = sumOfDivisor(d)
		if x== d and y==c :
			print(x,y)
			sum2 += (x+y)


print(sum2)
