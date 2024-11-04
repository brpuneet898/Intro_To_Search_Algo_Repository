import time
from helpers import get_neighbors, heuristic, goal_state
initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

def alpha_beta(state, depth, alpha, beta, is_maximizing):
    if state == goal_state:
        return 0 
    if depth == 0:
        return heuristic(state)
    if is_maximizing:
        max_eval = float('-inf')
        for next_state, _ in get_neighbors(state):
            eval = alpha_beta(next_state, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for next_state, _ in get_neighbors(state):
            eval = alpha_beta(next_state, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
start_time = time.time()
result = alpha_beta(initial_state, 5, float('-inf'), float('inf'), True)
end_time = time.time()
print("Alpha-Beta Pruning Result:", result)
print("Time taken:", end_time - start_time, "seconds")
