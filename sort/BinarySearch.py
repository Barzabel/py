class BinarySearch:
	def __init__(self,arr:list):
		self.arr = arr
		self.Left = 0
		self.Right = len(arr) - 1
		self.isSearch = 0

	def  Step(self, n:int):
		if self.isSearch != 0:
			return None

		index = (self.Right + self.Left)//2 

		if self.arr[index] == n or (self.Right == self.Left and self.arr[self.Left] == n):

			self.Left = index
			self.Right = index
			self.isSearch = 1

		elif self.Right - self.Left < 1:
			
			self.isSearch = -1

		elif self.arr[index] > n:
			self.Right = index - 1

		elif self.arr[index] < n:
			self.Left = index + 1

	def GetResult(self)->int:
		return self.isSearch 
