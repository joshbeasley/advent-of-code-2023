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

