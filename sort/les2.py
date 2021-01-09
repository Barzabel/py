def InsertionSortStep(array: list, step: int, i: int):
	sortarr = [array[x] for x in range(0,len(array),step) ]
	for x in range(0,len(sortarr)):
		for y in range(x):
			if sortarr[x] < sortarr[y]:
				sortarr[x],sortarr[y] = sortarr[y],sortarr[x]
				continue
	for x in range(0,len(array),step):
		array[x] = sortarr.pop(0)
	return array
