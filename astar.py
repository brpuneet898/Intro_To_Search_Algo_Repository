import time
import heapq
from helpers import get_neighbors, heuristic, goal_state
initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

def a_star(initial, goal):
    queue = [(heuristic(initial), 0, initial, [])]
    visited = set()
    visited.add(tuple(map(tuple, initial)))
    while queue:
        _, cost, state, path = heapq.heappop(queue)
        if state == goal:
            return path

        for next_state, move in get_neighbors(state):
            if tuple(map(tuple, next_state)) not in visited:
                visited.add(tuple(map(tuple, next_state)))
                new_cost = cost + 1
                heapq.heappush(queue, (new_cost + heuristic(next_state), new_cost, next_state, path + [move]))
    return None
start_time = time.time()
solution = a_star(initial_state, goal_state)
end_time = time.time()
print("A* Solution:", solution)
print("Time taken:", end_time - start_time, "seconds")

