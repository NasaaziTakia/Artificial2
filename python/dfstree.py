# QN 2a)
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

# No need for color, parent, or travelTime in tree search

dfsOutput = []

def dfsMethod(h):
    dfsOutput.append(h)
    for v, _ in adj_list[h]:
        dfsMethod(v)

# Start DFS from the "S" node
dfsMethod("S")

# Print the DFS traversal
print("DFS Output:", dfsOutput)
