a = 0
b = 1
sum = 0
for c in range(9999):

  a = b
  b = sum
  sum = (a + b)
 
  if len(str(sum)) == 1000:
    print(c +1)
    print(sum)
