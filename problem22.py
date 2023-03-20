#not right

listOfWord = ["AA","ACB", "LAC"]
mult_index_sum = 0
for b in range(len(listOfWord)):
	mult_index = 1 
	wordInList = listOfWord[b]
	print(b )

	sumOfWord = 0
	for c in range(len(wordInList)):
		sumOfWord += ((ord(wordInList[c])) - 64)
	print(sumOfWord)
	mult_index = sumOfWord*(b+1)
	mult_index_sum += mult_index
print(mult_index)
print(mult_index_sum)
