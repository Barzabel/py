def InsertionSortStep(array: list, step: int, i: int):
	sortarr = [array[x] for x in range(i,len(array),step) ]
	for x in range(0,len(sortarr)):
		for y in range(x):
			if sortarr[x] < sortarr[y]:
				sortarr[x],sortarr[y] = sortarr[y],sortarr[x]
				continue
	for x in range(i,len(array),step):
		array[x] = sortarr.pop(0)
	return array




def KnuthSequence(array_size: int ) -> list:
	if array_size == 0:
		return [1,]
	res = []
	i = 1
	while i <= array_size:
		res.append(i)
		i = 3 * i + 1
		
	res.reverse()
	return res


def sortshel(arr):
	knuth_sequence_forlen = KnuthSequence(len(arr))
	res = []
	for x in knuth_sequence_forlen:
		for n in range(x):
			res = InsertionSortStep(arr, x, n)

	return res
