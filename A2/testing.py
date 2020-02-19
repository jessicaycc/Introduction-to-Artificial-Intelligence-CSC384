import itertools
from itertools import permutations
import operator
from cspbase import *
dimension =5
dim = 5
'''
options = [tuple(range(1, dimension + 1))][:] * 3
print (options)
satisfying_tuples_cand = list(itertools.product(*options))
print (satisfying_tuples_cand)
cells=(23,23,23)
t =  list(itertools.product(range(1,dimension+1),repeat=len(cells)))
print (t)


function = "x" if dimension ==4 else "y"
print (function)
function = operator.add if operator == 0 else
                   operator.sub if operator == 1 else
                   operator.div if operator == 2 else
                   operator.mul



satisfying_tuples = []
for i in range(1, dimension + 1):
    for j in range(1, dimension + 1):
        if i != j:
            satisfying_tuples.append((i, j))
vars = []
flat_vars = []
for i in range(dimension):
    i_vars = []
    for j in range(dimension):
        name = str(i + 1) + str(j + 1)
        var = Variable(name, domain=range(1, dimension + 1))
        i_vars.append(var)
        flat_vars.append(var)
    vars.append(i_vars)
# row constraints
constraints = []
for row in range(dimension):
    for i in range(dimension):
        for j in range(dimension):
            if i < j:
                name = str(row + 1) + str(i + 1) + '_' + str(row + 1) + str(j + 1)
                c = Constraint(name, [vars[row][i], vars[row][j]])
                c.add_satisfying_tuples(satisfying_tuples[:])
                constraints.append(c)

# column constraints
for col in range(dimension):
    for i in range(dimension):
        for j in range(dimension):
            if i < j:
                name = str(i + 1) + str(col + 1) + '_' + str(j + 1) + str(col + 1)
                c = Constraint(name, [vars[i][col], vars[j][col]])
                c.add_satisfying_tuples(satisfying_tuples[:])
                constraints.append(c)
csp = CSP('binary_ne_grid', vars=flat_vars)


# add constraints
for c in constraints:
    csp.add_constraint(c)

csp.print_all()



satisfying_tuples = []
for i in range(1, dimension + 1):
    for j in range(1, dimension + 1):
        if i != j:
            satisfying_tuples.append((i, j))
print (satisfying_tuples)

satisfyingTuples = list(permutations(range(1,dim+1), 2))
print (satisfyingTuples)

var, oneDVar, cons = [], [], []
for row in range (dim):
       rowVar = []
       for column in range (dim):
           vari = Variable(str(row+1)+str(column+1), domain = range(1,dim+1))
           rowVar.append(vari) 
           oneDVar.append(vari)
       var.append(rowVar)


satisfyingTuples = list(permutations(range(1,dim+1), 2))
var, cons = [], []
oneDVar = []
for i in range(dimension):
    i_vars = []
    for j in range(dimension):
        name = str(i + 1) + str(j + 1)
        vari = Variable(name, domain=range(1, dimension + 1))
        i_vars.append(vari)
        oneDVar.append(vari)
    var.append(i_vars)

for row in range (1, dim+1):
       for col in range (1, dim+1):
           for i in range (1, dim+1):
               if col+i < dim+1:
                    rc = Constraint("{}{}-{}{}".format(row,col,row,col+i), [var[row-1][col-1],var[row-1][col]])
                    cc = Constraint("{}{}-{}{}".format(col,row,col+i,row), [var[col-1][row-1],var[col][row-1]])
                    rc.add_satisfying_tuples(satisfyingTuples[:])
                    cc.add_satisfying_tuples(satisfyingTuples[:])
                    cons.append(rc)
                    cons.append(cc)
csp = CSP('binary_ne_grid', vars = oneDVar)      

for c in cons:
    csp.add_constraint(c)   

csp.print_all()

'''
cells = [3,3,4]
combos =  list(itertools.product(range(1,dim+1),repeat=len(cells)))
print (combos)