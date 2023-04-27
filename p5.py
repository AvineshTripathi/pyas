import heapq

# Define the 4 possible movements in the grid (up, down, left, right)
movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define the heuristic function to estimate the distance between two points using Manhattan distance
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# Define the A* algorithm
def astar(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while len(frontier) > 0:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for movement in movements:
            next_node = (current[0] + movement[0], current[1] + movement[1])
            if next_node in graph:
                new_cost = cost_so_far[current] + graph[next_node]
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + heuristic(goal, next_node)
                    heapq.heappush(frontier, (priority, next_node))
                    came_from[next_node] = current

    return came_from, cost_so_far

# Example usage
# Define the graph as a dictionary where the keys are the grid points and the values are the costs to move to that point
graph = {
    (0, 0): 1,
    (0, 1): 3,
    (0, 2): 1,
    (1, 0): 1,
    (1, 1): 1,
    (1, 2): 1,
    (2, 0): 1,
    (2, 1): 1,
    (2, 2): 1
}

start = (0, 0)
goal = (2, 2)

came_from, cost_so_far = astar(graph, start, goal)

# Retrieve the shortest path
path = []
current = goal
while current != start:
    path.append(current)
    current = came_from[current]
path.append(start)
path.reverse()

print("Shortest path:", path)
print("Total cost:", cost_so_far[goal])
