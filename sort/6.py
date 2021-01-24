def ArrayChunk(array: list) -> int:
	res = len(array) // 2
	i1 = 0
	i2 = len(array) - 1

	r = array[res]
	
	while True:
		
		while array[i1] < r:
			i1 = i1 + 1
		
		while array[i2] > r:
			i2 = i2 - 1

		if i1 == i2-1 and array[i1] > array[i2]:

			array[i1] , array[i2] = array[i2] , array[i1]
			if array[i1] == r:
				res = i1
			elif array[i2] == r:
				res = i2
			i1 = 0
			i2 = len(array) - 1

		elif (i1 == i2) or (i1 == i2-1 and array[i1] < array[i2]):
			return res
		else:
			array[i1], array[i2] = array[i2], array[i1]
			if array[i1] == r:
				res = i1
			if array[i2] == r:
				res = i2

				
def QuickSort( array : list, left: int, right: int ) -> None:
	while left < right:

		arr = array[left:right + 1]
		pi = ArrayChunk(arr)
		array[left:right +1] = arr
		
		if pi < right - (left + pi):
			QuickSort(array, left, left + pi - 1 )
			left = left + pi + 1
		else:
			QuickSort(array, left + pi + 1, right )
			right = (left + pi -1  )
