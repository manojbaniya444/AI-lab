# G = {
#     "A": ["B", "C"],
#     "B": ["A","D","E"],
#     "C": ["A","F","G"],
#     "D":["B"],
#     "E":
#     "F":
#     "G":

# }

def getNextState(G, S):
    return G[S]

def DFS(G, start, goal):
    # initialize a stack to keep track of nodes
    stack = []

    # initialize a previous dictionary to keep track of previous node
    previous = {}

    # initializing a set to keep track of visited state
    visited = set()

    #push the initial state into the stack
    stack.append(start)

    #Set the previous of initial state to empty state
    previous[start] = ' '

    #do until the stack is empty
    while(stack):
        popped = stack.pop()
        visited.add(popped)

        if popped == goal:
            return True, previous
        for state in getNextState(G, popped):
            if state not in visited or state not in stack:
                stack.append(state)
                previous[state] = popped


    return False,previous
