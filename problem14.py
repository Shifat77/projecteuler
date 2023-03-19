#vul ache
for b in range(1,1000001):
  highest =1
  i = 1
  number = b
  while number !=1 :
    if number%2 ==0:
      seriesNum = number/2
    else:
      seriesNum = number *3 +1
    number = seriesNum
    i+= 1
  if highest <i :
    highest = i
    thatNum = b
    numOfElementOfSeries = highest
    
  # print(i)



print(thatNum)
print(numOfElementOfSeries)
