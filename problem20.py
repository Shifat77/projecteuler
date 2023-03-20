def factorial (number):
	factorialOfNumber = 1
	sumOfFactorialNumber = 0
	for a in range(1, number+1):
		factorialOfNumber *= a	
	return factorialOfNumber	

l = factorial(100)
print(l)

number = l
c = str(number)
sum = 0

for b in c:
	print(b + "+", end = '')
	
	sum += int(b)
	
print(" =")	
print(sum)
