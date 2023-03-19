def prime(number):
  def primeCheck (number):
    for x in range(2, number):
      y =  number%x
  
      if y == 0:
        return False
  if primeCheck (number) != False:
    return True


