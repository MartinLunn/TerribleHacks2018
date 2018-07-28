class Test_Manager:

	def __init__(self, test_functions, similarity_function=None):

		self.test_functions = test_functions

		self.PASS = 1
		self.FAIL = 0

		self.SAME = 0
		self.DIFF = 1

		self.EPS  = 1e-10

		if similarity_function is None:
			self.similarity_function = self.smape
		else:
			self.similarity_function = similarity_function

	def smape(self, a, b):
		return abs(a - b) / (abs(a) + abs(b) + self.EPS)

	def evaluate_test(self, test, compiled_code):
		try:
			passed, similarity = test(compiled_code, self.smape)

			if passed:
				return (self.PASS, err)
			else:
				return (self.FAIL, err)
		except:
			return (self.FAIL, self.DIFF)

	def evaluate_all_test(self, compiled_code):

		total_passed = 0
		total_error	 = 0

		for test_function in self.test_functions:
			p, e = test_function(compiled_code, self.smape)

			total_passed += p
			total_error  += e

		return (total_passed, total_error)