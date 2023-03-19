#more efficirnt code requre
input = 600851475143
for number in range (2, input):
  if input%number == 0:
    def prime(number):
      def primeCheck (number):
        for x in range(2, number):
          y =  number%x
      
          if y == 0:
            return False
      if primeCheck (number) != False:
        return True
    if prime(number) == True:
      print(number)
