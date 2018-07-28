from types import FunctionType
import random


def test_1(compiled_code, similarity_metric):

		a = random.randint(0,10)
		b = random.randint(0,10)

		expected = a + b - 1

		result = compiled_code(a, b)
		err    = similarity_metric(expected, result)

		# print(expected)
		# print(result)
		# print("///////////")

		return (result == expected, err)

def test_2(compiled_code, similarity_metric):

		a = random.randint(0,10)
		b = random.randint(0,10)

		expected = a + b - 1

		result = compiled_code(a, b)
		err    = similarity_metric(expected, result)

		# print(expected)
		# print(result)
		# print("///////////")

		return (result == expected, err)

class Tests:

	test_1 = test_1
	test_2 = test_2