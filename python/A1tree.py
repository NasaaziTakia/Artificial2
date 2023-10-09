# QN 2e)
class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

def depth_first_search_tree(graph, start, goal):
    open_stack = []
    closed_set = set()

    start_node = Node(state=start)
    open_stack.append(start_node)

    while open_stack:
        current_node = open_stack.pop()

        if current_node.state == goal:
            return reconstruct_path(current_node)

        if current_node.state in closed_set:
            continue

        closed_set.add(current_node.state)

        for neighbor in graph[current_node.state]:
            neighbor_node = Node(state=neighbor, parent=current_node)
            open_stack.append(neighbor_node)

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent
    return path

# Example usage:
if __name__ == "__main__":
    adj_list = {
        "A": ["B", "C"],
        "B": ["C"],
        "C": ["D", "G"],
        "D": ["G"],
        "G": [],
        "S": ["A", "B"]
    }

    start_node = 'S'
    goal_node = 'G'

    path = depth_first_search_tree(adj_list, start_node, goal_node)

    if path:
        print(f"Path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
