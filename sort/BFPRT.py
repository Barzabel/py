
def median(lst):
	n = len(lst)
	if n < 1:
		return None
	return lst[n//2]


def chunked(size, source):
	result = []
	index = 0
	while index < len(source):
		result.append(source[index:index + size])
		index += size
	return result


def BubbleSortStep(array: list) -> list:
	res = True
	for x , y in zip(range(0, len(array[:-1])), range(1,len(array))):
		if array[x] > array[y]:
			array[x], array[y] = array[y], array[x]
			res = False
	return res
def BubbleSort(array: list) -> list:
	issort = False
	while issort != True:
		issort = BubbleSortStep(array)

def ArrayChunk(array: list, el) -> int:

	res = len(array) // 2
	res2 = array.index(el)
	array[res2],array[res] = array[res],array[res2]


	r = el
	i1 = 0
	i2 = len(array) - 1

	
	
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







def KthOrderStatisticsStep( Array: list, L:int, R: int, k:int ) -> list:
	ar = chunked(5, Array[L:R])
	
	for x in range(len(ar)):
		
		BubbleSort(ar[x])
	mmed = []
	for x in ar:
		mmed.append(median(x))
	BubbleSort(mmed)
	s = median(mmed)
	
	i = ArrayChunk(Array,s)


	
	if i == k:
		return [i,i]
	if i > k:
		
		return [L,i] 
	if i < k:
		return [i,R] 

