for c in range(232792559, 232792563):
  y = 0
  for x in range(1, 21):
    if c % x != 0:
      y = 1

  if y == 0:
    print(c)
