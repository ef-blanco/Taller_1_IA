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
    respuesta = []
    explorados = []
    cola_prioridad = utils.PriorityQueue()
    s = Directions.SOUTH
    n = Directions.NORTH
    w = Directions.WEST
    e = Directions.EAST
    dict_direcciones = {"South":s,"North":n,"West":w,"East":e}
    
    # En la cola de prioridad se guardará una tupla donde el las primera posición se ecnontrará la posición (x,y) del robot
    # y en la segunda posición estará el costo total hasta dicha posición
    
    #Guardamos dentor de la tupla en 0:tupla de la posición en el mapa, 1:costo total al nodo y 2:camino a seguir para llegar al nodo desde el inicio
    cola_prioridad.push((problem.getStartState(),0,[]),0)
    
    alcanzo_goal = problem.isGoalState(problem.getStartState())
    while (not alcanzo_goal)or(not cola_prioridad.isEmpty):
        # Se saca el primer nodo el la cola de prioridad
        nodo_actual, costo_total, camino = cola_prioridad.pop()
        
        # Si sacó de la cola un nodo que ya visité antes, entonces sacó el siguiente en la cola
        if nodo_actual in explorados:
            nodo_actual, costo_total, camino = cola_prioridad.pop()
        
        # Miramos si ya llegamos al objetivo
        alcanzo_goal = problem.isGoalState(nodo_actual)
        if(alcanzo_goal):
            respuesta = camino
        # Se obtienen los sucesores del nodo en el que está actualmente el robot
        sucesores = problem.getSuccessors(nodo_actual)
        
        # Añadimos a la cola de prioridad todos los nodos vecinos con prioridad igual al peso total que toma llegar a ellos
        for sucesor in sucesores:
            if(sucesor[0] not in explorados):
                #Al añadir los sucesores:
                # 1 - sucesor: tupla de 2 posiciones con la pos en el mapa
                # 2 - costo total al sucesor
                # 3 - lista con las acciones que se deben tomar para llegar al sucesor con peso igual al valor en 2
                new_path = camino[:]
                new_path.append(dict_direcciones[sucesor[1]])
                
                cola_prioridad.push((sucesor[0],sucesor[2]+costo_total,new_path),sucesor[2]+costo_total)
        
        # Se marca como explorado el nodo en el que se sitúa el robot
        explorados.append(nodo_actual)
    
    return respuesta


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
