
# QN 2d) 
def depth_first_search_tree(adj_list, start, goal):
    visited = set()
    open_stack = [(start, None)]  # Tuple format: (current node, parent node)
    parent_map = {}
    
    while open_stack:
        node, parent = open_stack.pop()
        
        if node in visited:
            continue
        
        visited.add(node)
        
        if node == goal:
            print("Goal reached!")
            path = reconstruct_path(parent_map, start, goal)
            return path
        
        if node in adj_list:
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    open_stack.append((neighbor, node))
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
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["D", "G"],
    "D": ["G"],
    "G": [],
    "S": ["A", "B"]
}

start_node = "S"
goal_node = "G"

path = depth_first_search_tree(adj_list, start_node, goal_node)
if path:
    print("Tree Search Path from", start_node, "to", goal_node, "is:", " -> ".join(path))
else:
    print("No path found from", start_node, "to", goal_node)
