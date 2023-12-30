# setting the initial_state:
initial="WWWW" # west side of the river and in order of Farmer, Goat, Wolf, Cabbage respectively
goal="EEEE" # East side of the river and in order of Farmer, Goat, Wolf, Cabbage

# defining our valid states:
valid_states={"WWWW","EWWW","WEWW","WWEW","WWWE","WEEE","EWEE","EEWE","EEEW","EEWW","WWEE","EEEE"}

# transitions: move to west if on west and opposite for east
transitions = {
    "W":"E",
    "E":"W"
}
def river_cross(initial,goal):
    stack=[initial] # list of state
    visited = [initial] # list to keep tracl og visited states
    route = {initial: None} # dictionary to keep track of our route <"result state": "previous state">

    while stack:
        state = stack.pop()
        if state == goal: #if the goal is the same as in the state i.e we need EEEE then we return route list as solution which contain the total vaild move to reach the goal
            return True,route
        for i in range(0,4):
            if state[i] == state[0]: # this condition become true wheen the side of farmer is same as the side of object to be moved and as in our case farmer is at 0th position.so iam checking if the object is at the same side as farmer
                # if the farmer and object are in the same side then we can move the object to the opposite side using the transition dictionary
                next_state = list(state)
                next_state[i] =  next_state[0] = transitions[state[i]] #switching the side of the matched object
                next_state = "".join(next_state)

                # checking if the next state is not visited and is a valid state
                if next_state not in visited and next_state in valid_states:
                    stack.append(next_state)
                    route[next_state] = state
                    visited.append(next_state)
        
    return False, "No route found"

def reconstruct_path(route,goal):
    path = []
    while goal:
        path.append(goal)
        goal = route[goal]
    return path[::-1]

is_result_found, result = river_cross(initial, goal)
if is_result_found:
    print("Solution found")
    print(result)
    solution = reconstruct_path(result, goal)
    print("\n")
    print("The path is: ")
    print(solution)
else:
    print("No solution found")