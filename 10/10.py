file = open('maze.txt').read().splitlines()

grid = []
for line in file:
    grid.append([*line])

start = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i, j)
            grid[i, j] = 0
            
def get_neighbors(node):
    # top
    
    # bottom
    
    # left
    
    # right
            
explored = set([start])
queue = [start]

while len(q) > 0:
    curr = queue.pop(0)
    for neighbor in get_neighbors(curr):
        if neighbor not in explored:
            explored.add(neighbor)
            queue.append(neighbor)

