# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define a function to find the blank tile (0)
def find_blank_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Define a function to get all possible next states from the current state
def get_next_states(state):
    next_states = []
    blank_i, blank_j = find_blank_tile(state)

    # Move blank tile left
    if blank_j > 0:
        new_state = [row[:] for row in state]  # Make a deep copy of the current state
        new_state[blank_i][blank_j], new_state[blank_i][blank_j - 1] = new_state[blank_i][blank_j - 1], new_state[blank_i][blank_j]  # Swap blank tile with the tile to its left
        next_states.append(new_state)

    # Move blank tile right
    if blank_j < 2:
        new_state = [row[:] for row in state]
        new_state[blank_i][blank_j], new_state[blank_i][blank_j + 1] = new_state[blank_i][blank_j + 1], new_state[blank_i][blank_j]
        next_states.append(new_state)

    # Move blank tile up
    if blank_i > 0:
        new_state = [row[:] for row in state]
        new_state[blank_i][blank_j], new_state[blank_i - 1][blank_j] = new_state[blank_i - 1][blank_j], new_state[blank_i][blank_j]
        next_states.append(new_state)

    # Move blank tile down
    if blank_i < 2:
        new_state = [row[:] for row in state]
        new_state[blank_i][blank_j], new_state[blank_i + 1][blank_j] = new_state[blank_i + 1][blank_j], new_state[blank_i][blank_j]
        next_states.append(new_state)

    return next_states

 # DFS to find the solution
def dfs_eight_puzzle(state, depth_limit):
    if state == goal_state:
        return True

    if depth_limit == 0:
        return False

    next_states = get_next_states(state)

    for next_state in next_states:
        if dfs_eight_puzzle(next_state, depth_limit - 1):
            return True

    return False


initial_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
depth_limit = 20  

if dfs_eight_puzzle(initial_state, depth_limit):
    print("Solution found!")
else:
    print("Solution not found.")
