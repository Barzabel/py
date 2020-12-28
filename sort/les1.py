def SelectionSortStep(array, i):
	array[array[i:].index(min(array[i:])) + i], array[i] = array[i], min(array[i:])



def BubbleSortStep(array):
	for x , y in zip(range(0, len(array[:-1])), range(1,len(array))):
		if array[x] > array[y]:
			array[x], array[y] = array[y], array[x]






array = [1,3,2,4]
BubbleSortStep(array)
print(array)