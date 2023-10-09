# QN 1b)
from collections import deque

def best_first_search(adj_list, heuristic, start, goal):
    visited = set()
    priority_queue = [(heuristic[start], start)]  # Priority queue with (heuristic, node) tuples
    parent = {}

    while priority_queue:
        _, current_node = priority_queue.pop(0)

        if current_node == goal:
            print("Goal reached:", current_node)
            print("Path from", start, "to", goal, ":")
            print_path(parent, start, goal)
            return True

        if current_node not in visited:
            print("Visiting node:", current_node)
            visited.add(current_node)

            # Sort neighbors based on heuristic values
            neighbors = sorted(adj_list[current_node], key=lambda x: heuristic[x[0]])

            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    priority_queue.append((heuristic[neighbor], neighbor))
                    parent[neighbor] = current_node
    
    print("Goal not reached.")
    return False

def print_path(parent, start, goal):
    if start == goal:
        print(start, end=' ')
    elif goal not in parent:
        print("No path from", start, "to", goal)
    else:
        print_path(parent, start, parent[goal])
        print(goal, end=' ')

# Define the graph and heuristic values
adj_list = {
    "A": [["B", 2], ["C", 2]],
    "B": [["C", 3]],
    "C": [["D", 4], ["G", 4]],
    "D": [["G", 1]],
    "G": [],
    "S": [["A", 3], ["B", 1]]
}

heuristic = {
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0,
    'S': 7,
}

start_node = 'S'
goal_node = 'G'

# Perform Best-First Search
result = best_first_search(adj_list, heuristic, start_node, goal_node)

if result:
    print("Path found from", start_node, "to", goal_node)
else:
    print("No path found from", start_node, "to", goal_node)
