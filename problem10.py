def prime(number):
  def primeCheck (number):
    for x in range(2, number):
      y =  number%x
  
      if y == 0:
        return False
  if primeCheck (number) != False:
    return True


sum = 0
for number in range(2, 2000000):
  if prime(number) == True:
    sum += number

print(sum)
