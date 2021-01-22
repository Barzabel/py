

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
			
		




def QuickSort( array : list, left: int, right: int ) -> None:
	arr = array[left:right + 1]
	index = ArrayChunk(arr)
	array[left:right +1] = arr
	
	
	if len(array[left:left + index+1])>3:
		QuickSort( array,left, left + index )

	if len(array[left + index:right])>3:	
		QuickSort( array,left + index,right )
			
