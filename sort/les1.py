def SelectionSortStep(array, i):
	array[array[i:].index(min(array[i:])) + i], array[i] = array[i], min(array[i:])


def BubbleSortStep(array):
	res = True
	for x , y in zip(range(0, len(array[:-1])), range(1,len(array))):
		if array[x] > array[y]:
			array[x], array[y] = array[y], array[x]
			res = False
	return res






