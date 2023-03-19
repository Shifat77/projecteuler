maxNum = 10000
numOfDivisor = 500

for a in range(1, maxNum):
  sum = 0
  for b in range (1,a):
    sum += b
  # print(sum)
  sum2 =1
  for c in range (1, sum):
    if sum% c == 0:
      sum2 +=1

  if sum2 == numOfDivisor:
    print(sum)
      
