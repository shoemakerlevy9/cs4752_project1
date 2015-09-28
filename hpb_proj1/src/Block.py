class Block():
	def __init__(self,name, x, z):
		self.name = name
		self.x = x
		self.z = z

	def __repr__(self):
		return "Block(%s,%d,%d)"%(self.name,self.x,self.z)

