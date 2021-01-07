
"""
def InsertionSortStep(array, step: int, i: int):
	if (i + step) > (len(array)-1):
		return array
	sortarr = array[0:i]
	val = array.pop(i+step)
	indexprev = len(sortarr) 
	for x in sortarr:
		if val < x:
			indexprev = sortarr.index(x)
			break
	sortarr.insert(indexprev, val)	
	return sortarr + array[i:]
"""
def InsertionSortStep(array: list, step: int, i: int):
	index = i + step - 1
	val = array.pop(i)
	array[index], val = val, array[index]
	indexprev = len(array[:i])
	for x in array[:i]:
		if val < x:
			indexprev = array[:i].index(x)
			break

	array.insert(indexprev, val)
	return array
	
