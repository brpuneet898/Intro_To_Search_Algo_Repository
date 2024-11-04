import time
import heapq
from helpers import get_neighbors, heuristic, goal_state
initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

def best_first(initial, goal):
    queue = [(heuristic(initial), initial, [])]
    visited = set()
    visited.add(tuple(map(tuple, initial)))
    while queue:
        _, state, path = heapq.heappop(queue)
        if state == goal:
            return path

        for next_state, move in get_neighbors(state):
            if tuple(map(tuple, next_state)) not in visited:
                visited.add(tuple(map(tuple, next_state)))
                heapq.heappush(queue, (heuristic(next_state), next_state, path + [move]))
    return None
start_time = time.time()
solution = best_first(initial_state, goal_state)
end_time = time.time()
print("Best-First Solution:", solution)
print("Time taken:", end_time - start_time, "seconds")

