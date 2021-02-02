class ksort:
	def __init__(self):
		self.items = [None] *  ((ord('z') - ord('a') + 1)*100)

	def index(self, s:str)->int:
		if len(s) != 3:
			return -1

		if not(ord('z') >= ord(s[0]) and ord('a') <= ord(s[0])):
			return -1

		if not(s[1:].isdigit()):
			return -1 
		return (ord(s[0]) - ord('a')) * 100 + int(s[1:])
	
	def add(self, s: str)-> bool:
		i = self.index(s)
		if i < 0:
			return False

		self.items[i] = s		
		return True
