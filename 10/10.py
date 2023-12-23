import numpy as np

file = open('maze.txt').read().splitlines()

grid = []
for line in file:
    grid.append([*line])
    
# Part 1

start = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i, j)
            # grid[i, j] = 0
            
def get_neighbors(node):
    r, c = node
    val = grid[r][c]
    neighbors = []
    # grid[r-1][c]
    if r - 1 >= 0 and (val == 'S' or val == '|' or val == 'J' or val == 'L') and (grid[r-1][c] == '|' or grid[r-1][c] == '7' or grid[r-1][c] == 'F'):
        neighbors.append((r-1, c))
    # grid[r+1][c]
    if r + 1 < len(grid) and (val == 'S' or val == '|' or val == '7' or val == 'F') and (grid[r+1][c] == '|' or grid[r+1][c] == 'L' or grid[r+1][c] == 'J'):
        neighbors.append((r+1, c))
    # grid[r][c-1]
    if c - 1 >= 0 and (val == 'S' or val == '-' or val == '7' or val == 'J') and (grid[r][c-1] == '-' or grid[r][c-1] == 'L' or grid[r][c-1] == 'F'):
        neighbors.append((r, c-1))
    # grid[r][c+1]
    if c + 1 >= 0 and (val == 'S' or val == '-' or val == 'F' or val == 'L') and(grid[r][c+1] == '-' or grid[r][c+1] == 'J' or grid[r][c+1] == '7'):
        neighbors.append((r, c+1))
    return neighbors
            
explored = set([start])
queue = [start]
depth = {}
depth[start] = 0

while len(queue) > 0:
    curr = queue.pop(0)
    for neighbor in get_neighbors(curr):
        if neighbor not in explored:
            explored.add(neighbor)
            queue.append(neighbor)
            depth[neighbor] = depth[curr] + 1
            
print(max(depth.values()))

# Part 2

# Attempt 1: Shoelace and Pick's
# Pick's Thereom: i = A - (b/2) - 1 where b = length of loop and A = area
# Shoelace Formula: 2A = |x1 x2 x3 ... xn x1|      
#                        |y1 y2 y3 ... yn y1|

keys = list(depth.keys())
points = []
points.append(keys.pop(0))
left = True
while len(keys) > 0:
    if left:
        points.insert(0, keys.pop(0))
    else:
        points.append(keys.pop(0))
    left = not left
points.reverse()

x = []
y = []
for i, j in points:
    x += [i, i]
    y += [j, j]

x = x[1:] + [x[0]]
y = y[1:] + [y[0]]

squares = []
for i in range(0, len(x), 2):
    square = []
    square.append([x[i], x[i+1]])
    square.append([y[i], y[i+1]])
    squares.append(square)
    
area = np.sum(np.linalg.det(np.array(squares))) / 2
b = len(depth.keys())
i = area - (b/2) - 1

# Must be messing up the math here, going to try a more naive method

# Attempt 2: Vertical Bar Parity
inside = 0
for i in range(len(grid)):
    bars = 0
    for j in range(len(grid[0])):
        if grid[i][j] == '.' and bars % 2 == 1:
            inside += 1
        if (i, j) in depth and grid[i][j] in '|JL':
            bars += 1
print(inside)

