from test_manager import Test_Manager
from tests import Tests

test_manager = Test_Manager(Tests)

def test_individual(a, b):
	return a + b

print(test_manager.evaluate_all_tests(test_individual))