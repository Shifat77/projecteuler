def sumsqure(number):
  SumOfSqure = 0
  for x in range(1, number + 1):
    SumOfSqure += x * x

  return SumOfSqure


def squreSum(number):
  justSum = 0
  for x in range(1, number + 1):
    justSum += x
  return justSum * justSum


print(squreSum(100) - sumsqure(100))
