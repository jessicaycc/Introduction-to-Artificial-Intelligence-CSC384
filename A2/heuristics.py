'''
This file will contain different variable ordering heuristics to be used within
bt_search.

1. ord_dh(csp)
    - Takes in a CSP object (csp).
    - Returns the next Variable to be assigned as per the DH heuristic.
2. ord_mrv(csp)
    - Takes in a CSP object (csp).
    - Returns the next Variable to be assigned as per the MRV heuristic.
3. val_lcv(csp, var)
    - Takes in a CSP object (csp), and a Variable object (var)
    - Returns a list of all of var's potential values, ordered from best value 
      choice to worst value choice according to the LCV heuristic.

The heuristics can use the csp argument (CSP object) to get access to the 
variables and constraints of the problem. The assigned variables and values can 
be accessed via methods.
'''

import random
from copy import deepcopy
from math import inf
import operator
import itertools

def ord_dh(csp):
    maxi = -1
    branch = None
    list = []
    for v in csp.get_all_unasgn_vars():
        num = 0
        for c in csp.get_cons_with_var(v):
            num += c.get_n_unasgn() - 1
        if num > maxi:
            maxi = num
            branch = v
    return branch

def ord_mrv(csp):
    mini = inf
    branch = None
    for v in csp.get_all_unasgn_vars():
        if v.cur_domain_size() < mini: 
            mini = v.cur_domain_size()
            branch = v
    return branch 
  

def val_lcv(csp, var):
    vals = list()
    combos = []
    for value in var.cur_domain():
        pruned = 0
        for c in csp.get_cons_with_var(var):
            for v in c.get_scope():
                if v!=var:
                    combos.append(v.cur_domain())
                else:
                    combos.append([value])
            options =itertools.product(*combos)
            for i in options:
                if c.check(options) == True:
                    pruned+=1
            combos = []
        vals.append((value, pruned))
    return sort(vals)

def sort(vals):
    vals.sort(key=operator.itemgetter(1), reverse = True )
    lst = [x[0] for x in vals]
    return lst

