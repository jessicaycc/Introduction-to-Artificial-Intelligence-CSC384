'''
All models need to return a CSP object, and a list of lists of Variable objects 
representing the board. The returned list of lists is used to access the 
solution. 

For example, after these three lines of code

    csp, var_array = kenken_csp_model(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array[0][0].get_assigned_value() should be the correct value in the top left
cell of the KenKen puzzle.

The grid-only models do not need to encode the cage constraints.

1. binary_ne_grid (worth 10/100 marks)
    - A model of a KenKen grid (without cage constraints) built using only 
      binary not-equal constraints for both the row and column constraints.

2. nary_ad_grid (worth 10/100 marks)
    - A model of a KenKen grid (without cage constraints) built using only n-ary 
      all-different constraints for both the row and column constraints. 

3. kenken_csp_model (worth 20/100 marks) 
    - A model built using your choice of (1) binary binary not-equal, or (2) 
      n-ary all-different constraints for the grid.
    - Together with KenKen cage constraints.

'''
from cspbase import *
import itertools
import operator
from itertools import permutations
from functools import reduce

def binary_ne_grid(kenken_grid):
    
   dim = kenken_grid[0][0]
   var, oneDVar, cons = [], [], []

   satisfyingTuples = list(permutations(range(1,dim+1), 2))

   for row in range (dim):
       rowVar = []
       for column in range (dim):
           vari = Variable(str(row+1)+str(column+1), domain = range(1,dim+1))
           rowVar.append(vari) 
           oneDVar.append(vari)
       var.append(rowVar)

   for row in range (1, dim+1):
       for col in range (1, dim+1):
           for i in range (1, dim+1):
               if col+i < dim+1:
                    rc = Constraint("{}{}-{}{}".format(row,col,row,col+i), [var[row-1][col-1],var[row-1][col+i-1]])
                    cc = Constraint("{}{}-{}{}".format(col,row,col+i,row), [var[col-1][row-1],var[col+i-1][row-1]])
                    rc.add_satisfying_tuples(satisfyingTuples[:])
                    cc.add_satisfying_tuples(satisfyingTuples[:])
                    cons.append(rc)
                    cons.append(cc)

   csp = CSP('binary_ne_grid', vars = oneDVar)      

   for c in cons:
       csp.add_constraint(c)      

   return csp, var


def nary_ad_grid(kenken_grid):
    dim = kenken_grid[0][0]
    var, oneDVar, cons = list(), list(), list()
    
    satisfyingtuples = list(itertools.permutations(range(1, dim + 1)))

    for row in range (dim):
        rowVar = []
        for column in range (dim):
            vari = Variable(str(row+1)+str(column+1), domain = range(1,dim+1))
            rowVar.append(vari) 
            oneDVar.append(vari)
        var.append(rowVar)

    for i in range (dim):
        rc = Constraint("row_{}".format(i+1),var[i])
        c_vars = map(lambda x: x[i], var)
        cc = Constraint("col_{}".format(i+1),c_vars)
        rc.add_satisfying_tuples(satisfyingtuples[:])
        cc.add_satisfying_tuples(satisfyingtuples[:])
        cons.append(rc)
        cons.append(cc)
    
    csp = CSP("nary_ad_grid", vars = oneDVar)

    for c in cons:
        csp.add_constraint(c)

    return csp, var

def kenken_csp_model(kenken_grid):
    dim = kenken_grid[0][0]
    csp, var = binary_ne_grid(kenken_grid)
    #csp, var = nary_ad_grid(kenken_grid)
    cage = 0
    cage_vars, cons = [], []
    for lst in kenken_grid[1:]:
        #print ("cage", lst)
        if len(lst) == 2:
             cage_vars = [var[int(str(lst[0])[0])-1][int(str(lst[0])[1])-1]]
             satisfyingtuples = [(lst[1],)]
             #print (satisfyingtuples)
          
        else:
            cells = lst[:-2]
            op = lst[-1]
            target = lst[-2]
            cage_vars = []
            for i in cells:
                cage_vars.append(var[int(str(i)[0])-1][int(str(i)[1])-1])
            
            combos =  list(itertools.product(range(1,dim+1),repeat=len(cells)))
          
            satisfyingtuples = list()
          
            for x in combos:
                if op == 0 or op ==3:
                    function = operator.add if op == 0 else operator.mul
                    if reduce(function,x) == target:
                        satisfyingtuples.append(x)
                else:
                    choices = list(itertools.permutations(x))
                    function = operator.sub if op == 1 else operator.floordiv
                    for i in choices:
                        if reduce(function, i) == target:
                            satisfyingtuples.append(x)
                            break
        #print ("tuples", satisfyingtuples)
        cage+=1
        c = Constraint("cage_{}".format(cage),cage_vars)
        c.add_satisfying_tuples(satisfyingtuples)
        cons.append(c)

    for c in cons:
        csp.add_constraint(c)

    return csp, var



