from types import FunctionType

class Tests:

	def test_1(self, compiled_code, similarity_metric):

		a = 7
		b = 6

		expected = a + b - 1

		result = compiled_code(a, b)
		err    = similarity_metric(expected, result)

		return (result == expected, err)