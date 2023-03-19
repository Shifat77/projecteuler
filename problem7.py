def prime(number):

  def primeCheck(number):
    for x in range(2, number):
      y = number % x

      if y == 0:
        return False

  if primeCheck(number) != False:
    return True

y = 0
for number in range(1, 20000000):
  if prime(number) == True:
    # print(number)
    y +=1
    if y== (10001+1):
      print(number)
