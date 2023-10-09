# QN 2c)
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

def depth_first_search_tree(adj_list, start, goal):
    visited = set()
    parent_map = {}
    
    def dfs(node):
        visited.add(node)
        
        if node == goal:
            print("Goal reached!")
            path = reconstruct_path(parent_map, start, goal)
            return path
        
        for neighbor, _ in adj_list[node]:
            if neighbor not in visited:
                parent_map[neighbor] = node
                path = dfs(neighbor)
                if path:
                    return path
                
    path = dfs(start)
    
    if path:
        return path
    else:
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

start_node = "S"
goal_node = "G"

path = depth_first_search_tree(adj_list, start_node, goal_node)
if path:
    print("Path from", start_node, "to", goal_node, "is:", " -> ".join(path))
else:
    print("No path found from", start_node, "to", goal_node)
