def ArrayChunk(array: list) -> int:
	res = len(array) // 2
	i1 = 0
	i2 = len(array) - 1
	r = array[len(array) // 2]
	while True:
		
		while array[i1] < r:
			i1 += 1

		while array[i2] > r:
			i2 -= 1
		

		if  i1 == i2-1 and array[i1] > array[i2]:

			array[i1], array[i2] = array[i2], array[i1]
			i1 = 0
			i2 = len(array) - 1
			r = array[len(array) // 2]
			
		elif (i1 == i2) or (i1 == i2-1 and array[i1] < array[i2]):

			return res
		else:
			array[i1], array[i2] = array[i2], array[i1]
			if array[i1] == r:
				res = i1
			if array[i2] == r:
				res = i2
			
