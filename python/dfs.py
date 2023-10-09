# QN 1a)
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

color = {}
parent = {}
travelTime = {}
dfsOutput = []
time = 0  # Initialize time to 0

for node in adj_list.keys():
    color[node] = "w"
    parent[node] = "none"
    travelTime[node] = [-1, -1]  # Fix the syntax error here

def dfsMethod(h):
    global time
    color[h] = "g"
    travelTime[h][0] = time
    dfsOutput.append(h)
    for v, _ in adj_list[h]:
        if color[v] == "w":
            parent[v] = h
            time += 1
            dfsMethod(v)
    color[h] = "b"
    travelTime[h][1] = time
    time += 1

# Start DFS from the "S" node
dfsMethod("S")

# Print the DFS traversal
print("DFS Output:", dfsOutput)
