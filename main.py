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

from tests import Tests
from test_manager import Test_Manager

# =========================================================================
# ============================= Testing Code  =============================
# =========================================================================

test_manager = Test_Manager(Tests)

print(test_manager.test_functions)

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

pset = gp.PrimitiveSetTyped("MAIN", [float, float], float)

# boolean operators
# pset.addPrimitive(logic_and, [bool, bool], bool)
# pset.addPrimitive(logic_or, [bool, bool], bool)
# pset.addPrimitive(logic_not, [bool], bool)

pset.addPrimitive(add, [float,float], float)
pset.addPrimitive(sub, [float,float], float)
pset.addPrimitive(mul, [float,float], float)
pset.addPrimitive(div, [float,float], float)

# logic operators
# Define a new if-then-else function


# pset.addPrimitive(lt, [float, float], bool)
# pset.addPrimitive(eq, [float, float], bool)
# pset.addPrimitive(if_then_else, [bool, float, float], float)

# terminals
# pset.addEphemeralConstant("rand100", lambda: random.random() * 100, float)
# pset.addTerminal(False, bool)
# pset.addTerminal(True, bool)

creator.create("FitnessMax", base.Fitness, weights=(1.0, -1.0))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=0, max_=3)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

toolbox.register("evaluate", eval_tests)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=3)
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
	import matplotlib.pyplot as plt
	import networkx as nx
	import pygraphviz as pgv
	import graphviz
	from networkx.drawing.nx_agraph import graphviz_layout
	expr = gp.PrimitiveTree(hof[0])
	g = nx.Graph()
	nodes, edges, labels = gp.graph(expr)
	g.add_nodes_from(nodes)
	g.add_edges_from(edges)
	pos = graphviz_layout(g, prog="dot")

	nx.draw_networkx_nodes(g, pos)
	nx.draw_networkx_edges(g, pos)
	nx.draw_networkx_labels(g, pos, labels)
	plt.show()
