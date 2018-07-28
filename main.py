# =========================================================================
# ==============================  Imports  ================================
# =========================================================================

import types
import numpy
import random
import difflib
import itertools

import matplotlib.pyplot as plt
import networkx as nx
# import pygraphviz as pgv
import graphviz
from networkx.drawing.nx_agraph import graphviz_layout

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp

from tests import Tests
from sort_tests import Sort_Tests
from test_manager import Test_Manager

# =========================================================================
# ============================= Testing Code  =============================
# =========================================================================

def similarity_metric(a, b):

	return 1.0 - difflib.SequenceMatcher(None,a,b).ratio()

test_manager = Test_Manager(Sort_Tests, similarity_function=similarity_metric)

# =========================================================================
# =========================== Arithmetic Ops  =============================
# =========================================================================

def add(a, b):
	return a + b

def sub(a, b):
	return a - b

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

# =========================================================================
# ============================= Equality Ops  =============================
# =========================================================================

def lt(a, b):
	return a < b

def eq(a, b):
	return a == b

# =========================================================================
# ============================= Array Ops  ================================
# =========================================================================

def map_arr(arr, op):
	return map(op, arr)

def reduce_arr(arr, op):
	return reduce(op, arr)

def filter_arr(arr, op):
	return filter(op, arr)

def access_arr(arr, i):
	if len(arr) == 0:
		return 0
	return arr[i%len(arr)]

def store_arr(arr, i, v):
	if len(arr) == 0:
		return [v]
	arr[i%len(arr)] = v
	return arr

def append_arr(arr, v):
	return arr + [v]

def identity():
	return lambda x : x

def empty_arr():
	return []

# =========================================================================
# ================================  Utils  ================================
# =========================================================================

# def get_func(index):
# 	all_funcs = [
# 		add,
# 		sub,
# 		mul,
# 		div,
# 		logic_and,
# 		logic_or,
# 		logic_not,
# 		if_then_else,
# 		lt,
# 		eq,
# 		map_arr,
# 		reduce_arr,
# 		filter_arr,
# 		access_arr,
# 		store_arr
# 	]

# 	return all_funcs[index % len(all_funcs)]

def eval_tests(individual):

	global test_manager

	func = toolbox.compile(expr=individual)

	return test_manager.evaluate_all_tests(func)

# =========================================================================
# ========================== Define Primitives  ===========================
# =========================================================================

pset = gp.PrimitiveSetTyped("MAIN", [list], list)


# boolean operators
pset.addPrimitive(logic_and, [bool, bool], bool)
pset.addPrimitive(logic_or, [bool, bool], bool)
pset.addPrimitive(logic_not, [bool], bool)


pset.addPrimitive(access_arr, [list, int], int)
pset.addPrimitive(store_arr,  [list, int, int], list)
pset.addPrimitive(append_arr, [list, int], list)

# pset.addPrimitive(get_func, [int], types.FunctionType)
# pset.addPrimitive(map_arr, [list, types.FunctionType], list)
# pset.addPrimitive(reduce_arr, [list, types.FunctionType], float)
# pset.addPrimitive(filter_arr, [list, types.FunctionType], list)
# pset.addPrimitive(append_arr, [list, float], list)

# pset.addPrimitive(add, [float,float], float)
# pset.addPrimitive(sub, [float,float], float)
# pset.addPrimitive(mul, [float,float], float)
# pset.addPrimitive(div, [float,float], float)

pset.addPrimitive(lt, [int, int], bool)
pset.addPrimitive(eq, [int, int], bool)
pset.addPrimitive(if_then_else, [bool, int, int], int)

# pset.addEphemeralConstant("rand100", lambda: random.random() * 100, float)

# pset.addTerminal(1., float)
# pset.addTerminal([], list)
pset.addTerminal(False, bool)
pset.addTerminal(True, bool)

# =========================================================================
# =============================  Gen Algo  ================================
# =========================================================================

MAX_DEPTH = 5

creator.create("FitnessMax", base.Fitness, weights=(1.0, -1.0))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=0, max_=MAX_DEPTH)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

toolbox.register("evaluate", eval_tests)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=MAX_DEPTH)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

def main():
    random.seed(10)
    pop = toolbox.population(n=100)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    algorithms.eaSimple(pop, toolbox, 0.5, 0.2, 100, stats, halloffame=hof)

    return pop, stats, hof

if __name__ == "__main__":
	pop, stats, hof = main()


	arr = random.sample(range(1, 15), 10)

	expr = gp.PrimitiveTree(hof[0])

	print(expr)
	print("=============================")
	print(arr)
	print(sorted(arr))
	print(toolbox.compile(expr=expr)(arr))

	# g = nx.Graph()
	# nodes, edges, labels = gp.graph(expr)
	# g.add_nodes_from(nodes)
	# g.add_edges_from(edges)
	# pos = graphviz_layout(g, prog="dot")

	# nx.draw_networkx_nodes(g, pos)
	# nx.draw_networkx_edges(g, pos)
	# nx.draw_networkx_labels(g, pos, labels)
	# plt.show()
