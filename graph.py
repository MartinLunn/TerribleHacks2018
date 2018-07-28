import pandas
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

def inc(a):
	return a + 1


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

# =========================================================================
# =============================  Gen Algo  ================================
# =========================================================================

pset = gp.PrimitiveSetTyped("MAIN", [float] * 7, float)

# boolean operators
# pset.addPrimitive(logic_and, [bool, bool], bool)
# pset.addPrimitive(logic_or, [bool, bool], bool)
# pset.addPrimitive(logic_not, [bool], bool)

# pset.addPrimitive(inc, [float], float)

pset.addPrimitive(add, [float,float], float)
pset.addPrimitive(abs, [float], float)
pset.addPrimitive(sub, [float,float], float)
pset.addPrimitive(mul, [float,float], float)
pset.addPrimitive(div, [float,float], float)

# logic operators
# Define a new if-then-else function

# pset.addPrimitive(if_less_zero, [int, int, int], int)

pset.addPrimitive(lt, [float, float], bool)
pset.addPrimitive(eq, [float, float], bool)
pset.addPrimitive(if_then_else, [bool, float, float], float)

# terminals
pset.addEphemeralConstant("rand100", lambda: random.random() * 100, float)
pset.addTerminal(False, bool)
pset.addTerminal(True, bool)
pset.addTerminal(1, int)

# =========================================================================
# ================================  Load   ================================
# =========================================================================

toolbox = base.Toolbox()
toolbox.register("compile", gp.compile, pset=pset)

df = pandas.read_csv("./data.csv")

model = None

with open("model.tiny", "r") as f:
	model = f.read()

func = toolbox.compile(expr=model)

predictions = []

for row in df.iterrows():
	data = row[1].values.tolist()[1:-1]
	pred = func(*data)

	predictions += [pred]

df["predicted"] = pandas.Series(predictions)

df[["predicted", "MPG"]].plot()
plt.show()

