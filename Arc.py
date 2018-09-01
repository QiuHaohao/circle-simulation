from constants import *

class Arc:
	def __init__(self, r1, r2):
		self.r1 = r1
		self.r2 = r2
	def length(self):
		if self.r1 < self.r2:
			return self.r2 - self.r1
		else:
			return self.r2 + 2 * PI - self.r1
	def include(self, r):
		if self.r1 < self.r2:
			return self.r1 < r and self.r2 > r
		else:
			return self.r1 < r or self.r2 > r