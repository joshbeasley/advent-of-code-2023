import numpy as np

file = open('galaxies.txt').read().splitlines()

grid = []
for line in file:
    grid.append([*line])
    
grid = np.array(grid)

# Part 1

def expand(grid):
    row_idx = []
    col_idx = []
    for i in range(grid.shape[0]):
        if '#' not in grid[i]:
            row_idx.append(i + len(row_idx))
    for i in range(grid.shape[1]):
        if '#' not in grid[:, i]:
            col_idx.append(i + len(col_idx))
    
    for idx in row_idx:
        grid = np.insert(grid, idx, '.', 0)
        
    for idx in col_idx:
        grid = np.insert(grid, idx, '.', 1)
        
    return grid

grid = expand(grid)

galaxies = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            galaxies.append((i, j))

pairs = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

total = 0
for a, b in pairs:
    total += dist(a, b)

print(total)
    