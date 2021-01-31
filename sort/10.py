def MergeSort(array: list) -> list:
	if len(array) < 2:
		return array
	index = len(array) // 2

	left = MergeSort(array[index:])
	right = MergeSort(array[:index])
	res = []

	while len(left)>0 and len(right) > 0:
		if left[0] > right[0]:
			res.append(right.pop(0))
		else:
			res.append(left.pop(0))
	if len(left) > 0:
		res.extend(left)
	if len(right) > 0:
		res.extend(right)

	return res
