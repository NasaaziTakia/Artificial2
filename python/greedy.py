# QN 1d)
import heapq

def greedy_search(adj_list, heuristic, start, goal):
    visited = set()
    priority_queue = [(heuristic[start], start)]
    parent_map = {}
    
    while priority_queue:
        _, node = heapq.heappop(priority_queue)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        if node == goal:
            print("Goal reached!")
            path = reconstruct_path(parent_map, start, goal)
            return path
        
        for neighbor, _ in adj_list[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                parent_map[neighbor] = node
    
    print("Goal not reachable.")
    return []

def reconstruct_path(parent_map, start, goal):
    path = [goal]
    current = goal
    
    while current != start:
        if current not in parent_map:
            return []
        current = parent_map[current]
        path.append(current)
    
    return list(reversed(path))

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

start_node = "S"
goal_node = "G"

path = greedy_search(adj_list, heuristic, start_node, goal_node)
if path:
    print("Greedy Search Path from", start_node, "to", goal_node, "is:", " -> ".join(path))
else:
    print("No path found from", start_node, "to", goal_node)
