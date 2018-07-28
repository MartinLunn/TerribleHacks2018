from types import FunctionType
import random
import time

<<<<<<< HEAD
import pandas

def test_1(compiled_code, similarity_metric):

		data = pandas.read_csv("./data.csv")

		features = ["a_" + str(i + 1) for i in range(7)]

		for row in data.iterrows():
			data = row[1].values.tolist()[1:-1]
			mpg  = row[1].values.tolist()[0]

		expected = mpg
=======
random.seed(time.time())

def test_1(compiled_code, similarity_metric):

		n = 2

		arr = [1, 2]

		expected = sorted(arr)

		result = compiled_code(arr)
>>>>>>> ad69d090f391e3b83b16acb24fecdd955a1f1665

		result = compiled_code(*data)
		err    = similarity_metric(expected, result)

		return (result == expected, err)

class Sort_Tests:

	test_1 = test_1