# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    openlist = util.Stack()
    openlist.push([ [problem.getStartState()] , [None] ])

    while not openlist.isEmpty():
        node = openlist.pop()
        visited = node[0]
        actions = node[1]
        state = visited[-1]
        if (problem.isGoalState(state)):
            path = actions
            #print path
            return path[1:]
        for i in problem.getSuccessors(state):
            if i[0] not in visited:
                n = i[0]
                direction = i[1]     
                #print visited+[n]        
                openlist.push([ visited+[n] , actions+[direction] ])       
        
    return False  
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    openlist = util.Queue()
    visited = []
    openlist.push((problem.getStartState(),[]))
    visited.append(problem.getStartState())
    actions = []

    while not openlist.isEmpty():
        node = openlist.pop()
        state = node[0]
        actions = node [1]
        #print state 
        #print actions
        if (problem.isGoalState(state)):
            path = actions
            #print path
            return path
        for i in problem.getSuccessors(state):
            if i[0] not in visited:
                n = i[0]
                direction = i[1]
                visited.append(n)
                openlist.push((n,actions+[direction]))       
    return False
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    openlist = util.PriorityQueue()  
    openlist.push([problem.getStartState(),[]],0)
    seen = {problem.getStartState():0}

    actions = []

    while not openlist.isEmpty():
        node = openlist.pop()
        state = node[0]
        actions = node [1]
        if problem.getCostOfActions(actions) <= seen[state]:
            if (problem.isGoalState(state)):
                path = actions
                return path
            for i in problem.getSuccessors(state):
                if not i[0] in seen or problem.getCostOfActions(actions+[i[1]]) < seen[i[0]]:
                    n = i[0]
                    direction = i[1]
                    openlist.push([n,actions+[direction]],problem.getCostOfActions(actions+[direction]))  
                    seen[n] = problem.getCostOfActions(actions+[direction])     
    return False
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    openlist = util.PriorityQueue()  
    openlist.push([problem.getStartState(),[]], heuristic(problem.getStartState(), problem))
    seen = {problem.getStartState():0}
    actions = []

    while not openlist.isEmpty():
        state, actions = openlist.pop()
        totalCost = problem.getCostOfActions(actions) + heuristic(state,problem)
        if (problem.getCostOfActions(actions)) <= seen[state]:
            if (problem.isGoalState(state)):
                return actions
            for i in problem.getSuccessors(state):
                totalCost = problem.getCostOfActions(actions+[i[1]])+heuristic(i[0],problem)
                if not i[0] in seen or (totalCost) < seen[i[0]]:
                    n = i[0]
                    direction = i[1]
                    openlist.push([n,actions+[direction]],(problem.getCostOfActions(actions+[direction])+heuristic(n,problem)))
                    seen[n] = (problem.getCostOfActions(actions+[direction])+heuristic(n,problem))   
    return False
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
