import time
from collections import deque
from helpers import get_neighbors, goal_state
initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

def bfs(initial, goal):
    queue = deque([(initial, [])])  
    visited = set()
    visited.add(tuple(map(tuple, initial)))
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path

        for next_state, move in get_neighbors(state):
            if tuple(map(tuple, next_state)) not in visited:
                visited.add(tuple(map(tuple, next_state)))
                queue.append((next_state, path + [move]))
    return None
start_time = time.time()
solution = bfs(initial_state, goal_state)
end_time = time.time()
print("BFS Solution:", solution)
print("Time taken:", end_time - start_time, "seconds")
