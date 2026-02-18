from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # TODO: Add your code here
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    utils.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """
    costo_total = 0
    camino = []
    visitados = []
    cola_prioridad = utils.PriorityQueue()
    nodo_actual = problem.getStartState()
    s = Directions.SOUTH
    n = Directions.NORTH
    w = Directions.WEST
    e = Directions.EAST
    dict_direcciones = {"South":s,"North":n,"West":w,"East":e}
    
    while (not problem.isGoalState(nodo_actual)):
        # Se marca como visitado el nodo en el que se sitúa el robot
        visitados.append(nodo_actual)
        # Se obtienen los sucesores del nodo en el que está actualmente el robot
        sucesores = problem.getSuccessors(nodo_actual)
        # Añadimos a la cola de prioridad todos los nodos vecinos con prioridad igual a sus pesos (el peso que toma ir a ellos)
        for sucesor in sucesores:
            cola_prioridad.push(sucesor,sucesor[2])
        # Se saca el nodo al que se llega con menor costo y se le asigna al actual
        mejor_sucesor = cola_prioridad.pop()
        
        #Si el nodo ya fue visitado se vista el que le sigue
        while mejor_sucesor[0] not in visitados  and  not cola_prioridad.isEmpty():
            mejor_sucesor = cola_prioridad.pop()
        
        costo_total+=mejor_sucesor[2]
        camino.append(dict_direcciones[mejor_sucesor[1]])
        nodo_actual = mejor_sucesor[0]
        
        # Vaciamos la cola de prioridad para que en el proximo paso solo tengamos los sucesores del nuevo nodo
        while not cola_prioridad.isEmpty():
            elem = cola_prioridad.pop()
        
        return camino
        
        
        
    # TODO: Add your code here
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
