#        A
#     B       C
#   D    E       F
# G        H

graph = {
    "A": ["B", "c"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["H"],
    "F": [],
    "G": [],
    "H": []
}


stack = []
visited = []

def dfs_traverse(graph, start, visited):
    visited.append(start)
    stack.append(start)
    while stack:
        popped_node = stack.pop()
        print(popped_node)
        for neighbour_node in graph[popped_node]:
            if neighbour_node not in visited:
                visited.append(neighbour_node)
                stack.append(neighbour_node)
    return
dfs_traverse(graph,"A", visited)