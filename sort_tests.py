import random


def test_1(compiled_code, similarity_metric):

		n = 10

		arr = random.sample(range(1, 15), n)

		expected = sorted(arr)

		result = compiled_code(arr)

		err    = similarity_metric(expected, result)

		return (result == expected, err)

def test_2(compiled_code, similarity_metric):
		n = 10

		arr = random.sample(range(1, 15), n)

		expected = sorted(arr)

		result = compiled_code(arr)

		err    = similarity_metric(expected, result)

		return (result == expected, err)

def test_3(compiled_code, similarity_metric):

		n = 10

		arr = random.sample(range(1, 15), n)

		expected = sorted(arr)

		result = compiled_code(arr)

		err    = similarity_metric(expected, result)

		return (result == expected, err)

def test_4(compiled_code, similarity_metric):
		n = 10

		arr = random.sample(range(1, 15), n)

		expected = sorted(arr)

		result = compiled_code(arr)

		err    = similarity_metric(expected, result)

		return (result == expected, err)

def test_5(compiled_code, similarity_metric):

		n = 10

		arr = random.sample(range(1, 15), n)

		expected = sorted(arr)

		result = compiled_code(arr)

		err    = similarity_metric(expected, result)

		return (result == expected, err)

def test_6(compiled_code, similarity_metric):
		n = 10

		arr = random.sample(range(1, 15), n)

		expected = sorted(arr)

		result = compiled_code(arr)

		err    = similarity_metric(expected, result)

		return (result == expected, err)

class Sort_Tests:

	test_1 = test_1
	test_2 = test_2
	test_3 = test_3
	test_4 = test_4
	test_5 = test_5
	test_6 = test_6