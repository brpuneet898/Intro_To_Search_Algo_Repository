import time
from helpers import get_neighbors, goal_state
initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

def dfs(state, goal, path, visited):
    if state == goal:
        return path
    visited.add(tuple(map(tuple, state)))

    for next_state, move in get_neighbors(state):
        if tuple(map(tuple, next_state)) not in visited:
            result = dfs(next_state, goal, path + [move], visited)
            if result:
                return result
    return None

start_time = time.time()
solution = dfs(initial_state, goal_state, [], set())
end_time = time.time()
print("DFS Solution:", solution)
print("Time taken:", end_time - start_time, "seconds")
