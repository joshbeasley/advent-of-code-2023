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

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def to_tuple(grid):
    grid = [tuple(row) for row in grid]
    return tuple(grid)

def to_list(grid):
    grid = [list(row) for row in grid]
    return grid

def single_cycle(grid):
    for _ in range(4):
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    grid = roll_rock(i, j, grid)
        grid = list(zip(*grid))
        grid = [list(row[::-1]) for row in grid]
    return grid

seen = {to_tuple(grid)}
grids = [to_tuple(grid)]
count = 0
while True:
    count += 1
    grid = single_cycle(grid)
    grid = to_tuple(grid)
    if grid in seen:
        break
    seen.add(grid)
    grids.append(grid)
    grid = to_list(grid)

first = grids.index(grid)

grid = grids[(1000000000 - first) % (count - first) + first]

total = 0
for i in range(len(grid)):
    count = 0
    for j in range(len(grid[0])):
        if grid[i][j] == 'O':
            count += 1
    total += (len(grid) - i) * count
print(total)