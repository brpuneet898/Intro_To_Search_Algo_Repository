import time
from helpers import get_neighbors, heuristic, goal_state
initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

def minimax(state, depth, is_maximizing):
    if state == goal_state:
        return 0 
    if depth == 0:
        return heuristic(state)
    if is_maximizing:
        max_eval = float('-inf')
        for next_state, _ in get_neighbors(state):
            eval = minimax(next_state, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for next_state, _ in get_neighbors(state):
            eval = minimax(next_state, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval
start_time = time.time()
result = minimax(initial_state, 5, True)
end_time = time.time()
print("Minimax Result:", result)
print("Time taken:", end_time - start_time, "seconds")
