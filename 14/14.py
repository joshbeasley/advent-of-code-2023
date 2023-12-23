grid = open('platform.txt').read().splitlines()

new_grid = []
for i in range(len(grid)):
    new_grid.append([*grid[i]])
grid = new_grid

def top_count(r, c, grid):
    moves = 0
    for i in reversed(range(0, r)):
        if grid[i][c] != '.':
            break
        else:
            moves += 1
    return moves

def roll_rock(r, c, grid):
    count = top_count(r, c, grid)
    grid[r][c] = '.'
    grid[r-count][c] = 'O'
    return grid

for i in range(1, len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'O':
            grid = roll_rock(i, j, grid)

total = 0
for i in range(len(grid)):
    count = 0
    for j in range(len(grid[0])):
        if grid[i][j] == 'O':
            count += 1
    total += (len(grid) - i) * count
print(total)