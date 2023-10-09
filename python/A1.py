# QN 1e)
import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def total_cost(self):
        return self.cost + self.heuristic

    # Define a unique identifier for the node.
    def __lt__(self, other):
        return self.total_cost() < other.total_cost()

def a_star_search(graph, start, goal, heuristic):
    open_set = []
    closed_set = set()
    count = 0  # Unique identifier counter.

    start_node = Node(state=start, cost=0, heuristic=heuristic[start])
    heapq.heappush(open_set, (start_node.total_cost(), count, start_node))

    while open_set:
        _, _, current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            return reconstruct_path(current_node)

        if current_node.state in closed_set:
            continue

        closed_set.add(current_node.state)

        for neighbor, cost in graph[current_node.state]:
            count += 1
            neighbor_node = Node(state=neighbor, parent=current_node, cost=current_node.cost + cost, heuristic=heuristic[neighbor])
            heapq.heappush(open_set, (neighbor_node.total_cost(), count, neighbor_node))

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
        "A": [["B", 2], ["C", 2]],
        "B": [["C", 3]],
        "C": [["D", 4], ["G", 4]],
        "D": [["G", 1]],
        "G": [],
        "S": [["A", 3], ["B", 1]]
    }

    start_node = 'S'
    goal_node = 'G'

    heuristic = {
        'A': 5,
        'B': 7,
        'C': 4,
        'D': 1,
        'G': 0,
        'S': 7,
    }

    path = a_star_search(adj_list, start_node, goal_node, heuristic)

    if path:
        print(f"Shortest path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
