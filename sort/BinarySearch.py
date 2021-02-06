class BinarySearch:
	def __init__(self,arr:list):
		self.arr = arr
		self.Left = 0
		self.Right = len(arr) - 1
		self.isSearch = 0

	def _smal(self,n):
		for x in range(self.Left,self.Right + 1):
				if self.arr[x] == n:
					self.Left = x
					self.Right = x
					self.isSearch = 1
					return
		
		self.isSearch = -1

	def  Step(self, n:int):
		if self.isSearch != 0:
			return None

		if self.Right - self.Left < 2:
			self._smal(n)
			return

		index = (self.Right + self.Left)//2 

		if self.arr[index] == n or (self.Right == self.Left and self.arr[self.Left] == n):

			self.Left = index
			self.Right = index
			self.isSearch = 1

		elif self.Right - self.Left < 2:
			self._smal(n)
			return
			
		elif self.Right - self.Left < 1:
			self.isSearch = -1
			return

		elif self.arr[index] > n:
			self.Right = index -1
			if self.Right - self.Left < 2:
				self._smal(n)
			return

		elif self.arr[index] < n:
			self.Left = index + 1
			if self.Right - self.Left < 2:
				self._smal(n)
			return
		
	def GetResult(self)->int:
		return self.isSearch
	
def GallopingSearch(arr:list, n:int)->bool:
	i = 1
	index = int((2**i)-2)

	while (index < len(arr)-1) and (arr[index] < n)  :
		if index > len(arr)-1:
			index = len(arr) - 1
			break

		
		if arr[index] == n:
			return True
		i = i + 1
		index = int((2**i)-2)

	a = BinarySearch(arr)
	if index - 1 > len(arr):
		index = len(arr)
	a.Right = index 
	a.Left = int((2**(i-1))-2) 
	
	while a.GetResult() == 0:
		a.Step(n)

	if a.GetResult() == 1:
		return True
	else:
		return False

