# QN 1c)
import heapq
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
def uniform_cost_search(adj_list, heuristic, start, goal):
    visited = set()
    priority_queue = [(0, start)]
    parent_map = {}
    
    while priority_queue:
        cost, node = heapq.heappop(priority_queue)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        if node == goal:
            print("Goal reached!")
            path = reconstruct_path(parent_map, start, goal)
            return cost, path
        
        for neighbor, edge_cost in adj_list[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor))
                parent_map[neighbor] = node
    
    print("Goal not reachable.")
    return float('inf'), []

def reconstruct_path(parent_map, start, goal):
    path = [goal]
    current = goal
    
    while current != start:
        if current not in parent_map:
            return []
        current = parent_map[current]
        path.append(current)
    
    return list(reversed(path))

start_node = "S"
goal_node = "G"

cost, path = uniform_cost_search(adj_list, heuristic, start_node, goal_node)
if path:
    print("Path from", start_node, "to", goal_node, "is:", " -> ".join(path))
    print("Total cost of the path:", cost)
else:
    print("No path found from", start_node, "to", goal_node)

