# =========================================================================
# ==============================  Imports  ================================
# =========================================================================

import numpy
import random
import itertools

import matplotlib.pyplot as plt
import networkx as nx

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp

from sort_tests import Sort_Tests
from test_manager import Test_Manager

import time

random.seed(time.time())

# =========================================================================
# ============================= Testing Code  =============================
# =========================================================================

def error_metric(a, b):
	return (a-b)**2

test_manager = Test_Manager(Sort_Tests, similarity_function=error_metric)

# =========================================================================
# =========================== Arithmetic Ops  =============================
# =========================================================================

def add(a, b):
	return a + b

def neg(a):
	return -a

def mul(a, b):
	return a * b

def div(a, b):
	if b == 0:
		return 0.
	else:
		return a / b


# =========================================================================
# ============================= Boolean Ops  ==============================
# =========================================================================

def logic_and(a, b):
	return a and b

def logic_or(a, b):
	return a or b

def logic_not(a):
	return not a

def if_then_else(flag, output1, output2):
    if flag:
    	return output1
    else:
    	return output2

def if_less_zero(a, b, c):
	if a < 0:
		return b
	else:
		return c

# =========================================================================
# ============================= Equality Ops  =============================
# =========================================================================

def lt(a, b):
	return a < b

def eq(a, b):
	return a == b

# =========================================================================
# =============================== List Ops  ===============================
# =========================================================================

def get_arr(arr, index):
	if index >= len(arr):
		index = len(arr) - 1
	elif index < 0:
		index = 0
	return arr[index]

def swap_arr(arr, a, b):
	if a >= len(arr):
		a = len(arr) - 1
	elif a < 0:
		a = 0

	if b > len(arr):
		b = len(arr) - 1
	elif b < 0:
		b = 0

	t = a
	a = b
	b = t

	return arr

<<<<<<< HEAD
=======
def append_arr(arr, v):
	return arr + [v]

def identity():
	return lambda x : x

def empty_arr():
	return []

def increment(i):
	return i + 1

def decrement(i):
	return i - 1

def swap_arr(l, a, b):

	if len(l) == 0:
		return l

	n = len(l)

	temp = l[a%n]
	l[a%n] = l[b%n]
	l[b%n] = temp

	return l

def largest(a, b):
	if a > b:
		return a
	else:
		return b

>>>>>>> ad69d090f391e3b83b16acb24fecdd955a1f1665
# =========================================================================
# ================================  Utils  ================================
# =========================================================================

def eval_tests(individual):

	global test_manager
	# Transform the tree expression in a callable function
	func = toolbox.compile(expr=individual)

	return test_manager.evaluate_all_tests(func)

# =========================================================================
# =============================  Gen Algo  ================================
# =========================================================================

<<<<<<< HEAD
pset = gp.PrimitiveSetTyped("MAIN", [float] * 7, float)

pset.addPrimitive(add, [float,float], float)
pset.addPrimitive(neg, [float], float)
pset.addPrimitive(mul, [float,float], float)
pset.addPrimitive(div, [float,float], float)

pset.addPrimitive(lt, [float, float], bool)
pset.addPrimitive(if_then_else, [bool, float, float], float)

# terminals
pset.addEphemeralConstant("rand100", lambda: random.random() * 100, float)
pset.addTerminal(False, bool)
pset.addTerminal(True, bool)

creator.create("FitnessMax", base.Fitness, weights=(-1.0, -1.0))
=======
pset = gp.PrimitiveSetTyped("MAIN", [list], list)

pset.addPrimitive(access_arr, [list, int], int)
pset.addPrimitive(store_arr, [list, int, int], list)

pset.addPrimitive(sub, [int, int], int)
pset.addPrimitive(largest, [int, int], int)

pset.addPrimitive(increment, [int], int)
pset.addPrimitive(decrement, [int], int)

# pset.addPrimitive(lt, [int, int], bool)
# pset.addPrimitive(if_then_else, [bool, int, int], int)

# pset.addTerminal(False, bool)
# pset.addTerminal(True, bool)
pset.addTerminal(0, int)
# pset.addTerminal(1, int)

# =========================================================================
# =============================  Gen Algo  ================================
# =========================================================================

MAX_DEPTH = 1

creator.create("FitnessMax", base.Fitness, weights=(1.0, -1.0))
>>>>>>> ad69d090f391e3b83b16acb24fecdd955a1f1665
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=0, max_=15)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

toolbox.register("evaluate", eval_tests)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genHalfAndHalf, min_=0, max_=15)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

def main():
<<<<<<< HEAD
	pop = toolbox.population(n=200)
	hof = tools.HallOfFame(1)
	stats = tools.Statistics(lambda ind: ind.fitness.values)
	stats.register("avg", numpy.mean)
	stats.register("std", numpy.std)
	stats.register("min", numpy.min)
	stats.register("max", numpy.max)

	try:
		algorithms.eaSimple(pop, toolbox, 0.5, 0.2, 100, stats, halloffame=hof)
	except:
		pass
=======
    pop = toolbox.population(n=100)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    algorithms.eaMuPlusLambda(pop, toolbox, 100, 100, 0.25, 0.25, 100, stats, halloffame=hof)
>>>>>>> ad69d090f391e3b83b16acb24fecdd955a1f1665

	return pop, stats, hof

if __name__ == "__main__":
	pop, stats, hof = main()

	expr = gp.PrimitiveTree(hof[0])

	print(expr)
<<<<<<< HEAD
=======
	# print("=============================")
	# for i in range(5):
	# 	print("-----------")
	# 	arr = []
	# 	for i in range(2):
	# 		arr += [random.randint(0,10)]
	# 	print(arr)
	# 	print(sorted(arr))
	# 	print(toolbox.compile(expr=expr)(arr))

	# g = nx.Graph()
	# nodes, edges, labels = gp.graph(expr)
	# g.add_nodes_from(nodes)
	# g.add_edges_from(edges)
	# pos = graphviz_layout(g, prog="dot")

	# nx.draw_networkx_nodes(g, pos)
	# nx.draw_networkx_edges(g, pos)
	# nx.draw_networkx_labels(g, pos, labels)
	# plt.show()
>>>>>>> ad69d090f391e3b83b16acb24fecdd955a1f1665
