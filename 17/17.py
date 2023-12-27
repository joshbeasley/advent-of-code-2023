import queue

grid = open('map.txt').read().splitlines()

def get_steps(new_direction, direction, steps):
    new_steps = 1
    if new_direction == direction:
        new_steps = steps + 1
    return new_steps

def valid_steps(steps):
    return True if steps <= 3 else False

def get_children(state):
    r, c, direction, steps = state
    new_steps = None
    children = []
    
    if r + 1 < len(grid):
        new_steps = get_steps("down", direction, steps)
        if valid_steps(new_steps):
            children.append((r+1, c, "down", new_steps))
    if r - 1 >= 0:
        new_steps = get_steps("up", direction, steps)
        if valid_steps(new_steps):
            children.append((r-1, c, "up", new_steps))
    if c + 1 < len(grid[0]):
        new_steps = get_steps("right", direction, steps)
        if valid_steps(new_steps):
            children.append((r, c+1, "right", new_steps))
    if c - 1 >= 0:
        new_steps = get_steps("left", direction, steps)
        if valid_steps(new_steps):
            children.append((r, c-1, "left", new_steps))
    return children

visited = set()
frontier = queue.PriorityQueue()
parent = {}
cost_dict = {}

# state = (r, c, direction, num_steps)
initial = (0, 0, "right", 0)
frontier.put((0, initial))
parent[initial] = None
cost_dict[(initial[0], initial[1])] = 0

# Djikstra's Algorithm
while not frontier.empty():
    cost, state = frontier.get()
    r, c, direction, steps = state
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        print(cost + int(grid[-1][-1]))
    if (r, c) not in visited:
        visited.add((r, c))
        for child in get_children(state):
            cr, cc, cdirection, csteps = child
            parent[child] = state
            if (cr, cc) not in visited:
                new_cost = cost + int(grid[cr][cc])
                cost_dict[(cr, cc)] = new_cost
                frontier.put((new_cost, child))
            elif (cr, cc) in cost_dict:
                if cost + int(grid[cr][cc]) <= cost_dict[(cr, cc)]:
                    new_cost = cost + int(grid[cr][cc])
                    cost_dict[(cr, cc)] = new_cost
                    frontier.put((new_cost, child))
        
curr = (12, 12, 'down', 3)
path = [(12, 12, 'down', 3)]
while curr is not None:
    curr = parent[curr]
    path.append(curr)

print(list(reversed(path)))
    

