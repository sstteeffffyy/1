from random import random

class LinearRegression:
	def __init__(self, dim, loss, l1_coef, l2_coef):
		self.w = [random() for i in range(dim)]
		self.dim = dim
		self.loss = loss
		self.l1_coef = l1_coef
		self.l2_coef = l2_coef

	def fit(self, X, y):
		pass

	def predict(self, X, y):
		pass
