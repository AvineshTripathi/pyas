from queue import Queue

# Define a function to check if the current state is a goal state
def is_goal_state(state, target):
    return state[0] == target or state[1] == target

#  possible next states from the current state
def get_next_states(state, capacities):
    a, b = state
    a_capacity, b_capacity = capacities
    next_states = []

    # Fill A jug
    if a < a_capacity:
        next_states.append((a_capacity, b))
    # Fill B jug
    if b < b_capacity:
        next_states.append((a, b_capacity))
    # Empty A jug
    if a > 0:
        next_states.append((0, b))
    # Empty B jug
    if b > 0:
        next_states.append((a, 0))
    # Pour water from A to B
    if a > 0 and b < b_capacity:
        pour_amount = min(a, b_capacity - b)
        next_states.append((a - pour_amount, b + pour_amount))
    # Pour water from B to A
    if b > 0 and a < a_capacity:
        pour_amount = min(b, a_capacity - a)
        next_states.append((a + pour_amount, b - pour_amount))

    return next_states

# Define a function to perform BFS to find the solution
def bfs_water_jug(capacities, start, target):
    visited = set()  # Set to keep track of visited states
    queue = Queue()  # Queue for BFS traversal
    queue.put(start)  # Add the starting state to the queue

    while not queue.empty():
        current_state = queue.get()
        if current_state in visited:
            continue

        visited.add(current_state)

        if is_goal_state(current_state, target):
            return True

        next_states = get_next_states(current_state, capacities)

        for next_state in next_states:
            if next_state not in visited:
                queue.put(next_state)

    return False

# Example usage:
capacities = (4, 3)  # Capacities of the jugs
start_state = (0, 0)  # Starting state of the jugs
target_volume = 2  # Target volume to be measured
is_possible = bfs_water_jug(capacities, start_state, target_volume)

if is_possible:
    print("Target volume", target_volume, "is possible to measure.")
else:
    print("Target volume", target_volume, "is not possible to measure.")
