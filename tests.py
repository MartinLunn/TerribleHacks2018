from types import FunctionType
import random


def test_1(compiled_code, similarity_metric):

		a = 2
		b = 9

		expected = a

		result = compiled_code(a, b)
		err    = similarity_metric(expected, result)

		# print(expected)
		# print(result)
		# print("///////////")

		return (result == expected, err)

def test_2(compiled_code, similarity_metric):

		a = 8
		b = 3

		expected = b

		result = compiled_code(a, b)
		err    = similarity_metric(expected, result)

		return (result == expected, err)

def test_3(compiled_code, similarity_metric):

		a = 4
		b = 5

		expected = a

		result = compiled_code(a, b)
		err    = similarity_metric(expected, result)

		return (result == expected, err)

class Tests:

	test_1 = test_1
	test_2 = test_2