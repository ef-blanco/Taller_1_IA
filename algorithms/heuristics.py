from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    # TODO: Add your code here
    
    estadoActual = state
    estadoMeta = problem.goal()

    manhathan = abs(estadoActual[0] - estadoMeta[0]) + abs(estadoActual[1] - estadoMeta[1])
    return manhathan


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    estadoInicial = state
    estadoMeta = problem.goal()
    euclidiana = ((estadoInicial[0] - estadoMeta[0]) ** 2 + (estadoInicial[1] - estadoMeta[1]) ** 2) ** 0.5
    return euclidiana
    utils.raiseNotDefined()


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    # TODO: Add your code here
    posicion, grid = state
    sobrevivientes = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                sobrevivientes.append((i, j))

    if not sobrevivientes:
        return 0

    distancia_minima = min(abs(posicion[0] - s[0]) + abs(posicion[1] - s[1])
                           for s in sobrevivientes)


    if len(sobrevivientes) == 1:
        mst_cost = 0
    else:
        import heapq

        visited = set()
        heap = []
        start = sobrevivientes[0]
        visited.add(start)

        for s in sobrevivientes[1:]:
            dist = abs(start[0] - s[0]) + abs(start[1] - s[1])
            heapq.heappush(heap, (dist, start, s))

        mst_cost = 0
        while heap and len(visited) < len(sobrevivientes):
            dist, s1, s2 = heapq.heappop(heap)
            if s2 not in visited:
                visited.add(s2)
                mst_cost += dist
                for s in sobrevivientes:
                    if s not in visited:
                        new_dist = abs(s2[0] - s[0]) + abs(s2[1] - s[1])
                        heapq.heappush(heap, (new_dist, s2, s))

    return distancia_minima + mst_cost