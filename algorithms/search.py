from hashlib import new
from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic
import time


#Pongo esta vaina para calcular las complejidades jiji gracias chat por tanto 
def imprimir_resultado(nombre, T_formula, S_formula, nodos_expandidos, memoria_maxima):
    print(f"\n--- [ANÁLISIS DE {nombre}] ---")
    print(f"1. Temporal: {T_formula} => {nodos_expandidos} operaciones")
    print(f"2. Espacial: {S_formula} => {memoria_maxima} nodos en memoria")
    print("-" * 30)
    
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
    pila = utils.Stack()
    visitados = set()
    nodos_expandidos = 0
    max_memoria = 0
    

    estadoInicial = problem.getStartState()
    pila.push((estadoInicial, []))

    while not pila.isEmpty():
        max_memoria = max(max_memoria, len(visitados) + len(pila.list))
        estadoActual, camino = pila.pop()

        if problem.isGoalState(estadoActual):
            imprimir_resultado("DFS", "O(b^m)", "O(b * m)", nodos_expandidos, max_memoria)
            return camino

        if estadoActual not in visitados:
            nodos_expandidos += 1
            visitados.add(estadoActual)

            for sucesor, accion, costo in problem.getSuccessors(estadoActual):
                pila.push((sucesor, camino + [accion]))

    return []    
    
    

def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # TODO: Add your code here
    cola = utils.Queue()
    visitados = set()
    estadoInicial = problem.getStartState()
    cola.push((estadoInicial, []))
    nodos_expandidos = 0
    max_memoria = 0
    

    while not cola.isEmpty():
        max_memoria = max(max_memoria, len(visitados) + len(cola.list))
        estadoActual, camino = cola.pop()

        if problem.isGoalState(estadoActual):
            imprimir_resultado("BFS", "O(b^d)", "O(b^d)", nodos_expandidos, max_memoria)
            return camino

        if estadoActual not in visitados:

            visitados.add(estadoActual)
            nodos_expandidos += 1
            for sucesor, accion, costo in problem.getSuccessors(estadoActual):
                cola.push((sucesor, camino + [accion]))

    return []


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """
    #variable para el calculo de complejidades
    inicio_t = time.time()    
    nodos_expandidos = 0
    max_memoria = 0
    estadoInicial = problem.getStartState()
    colaPrioridad = utils.PriorityQueue()
    colaPrioridad.push((estadoInicial, [], 0), 0)
    mejorCosto = {}

    while not colaPrioridad.isEmpty():
        
        memoria_actual = len(mejorCosto) + len(colaPrioridad.heap)
        if memoria_actual > max_memoria:
            max_memoria = memoria_actual
        estadoActual, camino, costoActual = colaPrioridad.pop()

        if estadoActual in mejorCosto and costoActual > mejorCosto[estadoActual]:
            continue

        mejorCosto[estadoActual] = costoActual
        nodos_expandidos += 1

        if problem.isGoalState(estadoActual):
            imprimir_resultado("UCS", "O(b^(C*/ε))", "O(b^(C*/ε))", nodos_expandidos, max_memoria)
            return camino

        for sucesor, accion, costo in problem.getSuccessors(estadoActual):
            nuevoCamino = camino + [accion]
            nuevoCosto = costoActual + costo
            colaPrioridad.push((sucesor, nuevoCamino, nuevoCosto), nuevoCosto)

    return []


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    tiempoInicio = time.time()
    nodos_expandidos = 0
    max_memoria = 0
    estadoInicial = problem.getStartState()
    colaPrioridad = utils.PriorityQueue()
    colaPrioridad.push((estadoInicial, [], 0), heuristic(estadoInicial, problem))
    mejorCosto = {}
    nodos_expandidos = 0
    
    while not colaPrioridad.isEmpty():
        estadoActual, camino, costoActual = colaPrioridad.pop()

        if estadoActual in mejorCosto and costoActual > mejorCosto[estadoActual]:
            continue
        mejorCosto[estadoActual] = costoActual
        nodos_expandidos += 1
        max_memoria = max(max_memoria, len(mejorCosto))

        if problem.isGoalState(estadoActual):
            imprimir_resultado("A*", "O(b^(C*/ε))", "O(b^(C*/ε))", nodos_expandidos, max_memoria)
            return camino

        for sucesor, accion, costo in problem.getSuccessors(estadoActual):
            nuevoCamino = camino + [accion]
            nuevoCosto = costoActual + costo
            prioridad = nuevoCosto + heuristic(sucesor, problem)
            colaPrioridad.push((sucesor, nuevoCamino, nuevoCosto), prioridad)
    
    tiempoFin = time.time()
    print("Tiempo de ejecución: {:.2f} segundos".format(tiempoFin - tiempoInicio), "segundos")
    return []
    
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
