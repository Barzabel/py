def ArrayChunk(array: list) -> int:
	res = len(array) // 2
	i1 = 0
	i2 = len(array) - 1

	while True:
		i1 = 0
		i2 = len(array) - 1
		r = array[ res ]
		while array[i1] < r:
			i1 += 1

		while array[i2] > r:
			i2 -= 1
		if  i1 == i2-1 and array[i1] > array[i2]:
			array[i1], array[i2] = array[i2], array[i1]
			continue
		if (i1 == i2) or (i1 == i2-1 and array[i1] < array[i2]):
			return res
		
		array[i1], array[i2] = array[i2], array[i1]
