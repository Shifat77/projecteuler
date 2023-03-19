#more efficirnt code requre
number = 600851475143
x = 1

for x in range(1, number):

  x -= number
  x = abs(x)

  if number % x == 0:

    def prime(x):

      def primeCheck(x):
        for k in range(2, x):
          y = x % k

          if y == 0:
            return False

      if primeCheck(x) != False:
        return True

    if prime(x) == True:
      print(x)
