from types import FunctionType

class Test_Manager:

	def __init__(self, test_class, similarity_function=None):

		self.test_functions = [y for x, y in test_class.__dict__.items() if callable(y)]

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
				return (self.PASS, similarity)
			else:
				return (self.FAIL, similarity)
		except Exception as e:
			print(e)
			return (self.FAIL, self.DIFF)

	def evaluate_all_tests(self, compiled_code):


		total_passed = 0
		total_error	 = 0

		for test_function in self.test_functions:

			p, e = self.evaluate_test(test_function, compiled_code)

			total_passed += p
			total_error  += e

		return (total_passed, total_error)