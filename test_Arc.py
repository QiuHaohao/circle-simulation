from Arc import Arc
from constants import *

class TestClass(object):
	def calculate_length_correctly(self, r1, r2, length):
		arc = Arc(r1, r2)
		assert length == arc.length()
	def include_correctly(self, r1, r2, target, include):
		assert include == Arc(r1, r2).include(target)

	def test_length_no_wrap(self):
		self.calculate_length_correctly(0.5, 1, 0.5)
		self.calculate_length_correctly(0.5 * PI, 1.8 * PI, 1.3 * PI)

	def test_length_with_wrap(self):
		self.calculate_length_correctly(0.3 * PI, 0.2 * PI, 1.9 * PI)
		self.calculate_length_correctly(1.9 * PI, 0.2 * PI, 0.3 * PI)
	def test_include_no_wrap(self):
		self.include_correctly(0.5, 1, 0.75, True)
		self.include_correctly(0.5, 1, 0.4, False)
		self.include_correctly(0.5, 1, 1.6, False)

		self.include_correctly(0.5 * PI, 1.8 * PI, 1.3 * PI, True)
		self.include_correctly(0.5 * PI, 1.8 * PI, 0.3 * PI, False)
		self.include_correctly(0.5 * PI, 1.8 * PI, 1.9 * PI, False)