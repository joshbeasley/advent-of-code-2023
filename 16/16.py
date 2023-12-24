grid = open('grid.txt').read().splitlines()


def sim(r, c, dr, dc):
    seen = set()
    q = []

    # iterative approach
    initial = (r, c, dr, dc)
    q.append(initial)

    while len(q) > 0:
        r, c, dr, dc = q.pop(0)
        
        r += dr
        c += dc
        
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue
        
        val = grid[r][c]
        
        if val == '.' or (val == '-' and dc != 0) or (val == '|' and dr != 0):
            if (r,c,dr,dc) not in seen:
                q.append((r,c,dr,dc))
                seen.add((r,c,dr,dc))
        elif val == '\\':
            dr, dc = dc, dr
            if (r,c,dr,dc) not in seen:
                q.append((r,c,dr,dc))
                seen.add((r,c,dr,dc))
        elif val == '/':
            dr, dc = -dc, -dr
            if (r,c,dr,dc) not in seen:
                q.append((r,c,dr,dc))
                seen.add((r,c,dr,dc))
        else:
            if val == '|':
                for dr, dc in [(1, 0), (-1, 0)]:
                    if (r,c,dr,dc) not in seen:
                        q.append((r,c,dr,dc))
                        seen.add((r,c,dr,dc))   
            else:
                for dr, dc in [(0, 1), (0, -1)]:
                    if (r,c,dr,dc) not in seen:
                        q.append((r,c,dr,dc))
                        seen.add((r,c,dr,dc)) 

    return len(set([(i[0], i[1]) for i in seen]))

max_val = 0
for i in range(len(grid)):
    max_val = max(max_val, sim(i, -1, 0, 1))
    max_val = max(max_val, sim(i, len(grid[0]), 0, -1))

for i in range(len(grid[0])):
    max_val = max(max_val, sim(-1, i, 1, 0))
    max_val = max(max_val, sim(len(grid), i, -1, 0))
    
print(max_val)

# recursive approach
def energized(r, c, direction):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return 0
    if (r,c, direction) in seen:
        return 0
    seen.add((r,c, direction))
    if grid[r][c] == '.' or ((direction == 'left' or direction == 'right') and grid[r][c] == '-') or ((direction == 'up' or direction =='down') and grid[r][c] == '|'):
        if direction == 'up':
            return 1 + energized(r-1, c, 'up')
        if direction == 'down':
            return 1 + energized(r+1, c, 'down')
        if direction =='left':
            return 1 + energized(r, c-1, 'left')
        if direction == 'right':
            return 1 + energized(r, c+1, 'right')
    if grid[r][c] == "\\":
        if direction == 'up':
            return 1 + energized(r, c-1, 'left')
        if direction == 'down':
            return 1 + energized(r, c+1, 'right')
        if direction =='left':
            return 1 + energized(r-1, c, 'up')
        if direction == 'right':
            return 1 + energized(r+1, c, 'down')
    if grid[r][c] == '/':
        if direction == 'up':
            return 1 + energized(r, c+1, 'right')
        if direction == 'down':
            return 1 + energized(r, c-1, 'left')
        if direction =='left':
            return 1 + energized(r+1, c, 'down')
        if direction == 'right':
            return 1 + energized(r-1, c, 'up')
    if grid[r][c] == '|' and (direction == 'left' or direction == 'right'):
        return 1 + energized(r-1, c, 'up') + energized(r+1, c, 'down')
    if grid[r][c] == '-' and (direction == 'up' or direction == 'down'):
        return 1 + energized(r, c-1, 'left') + energized(r, c+1, 'right')

# energized(0,0,'right')
# print(seen)
# print(len(seen))
# print(len(set([(i[0], i[1]) for i in seen])))

    
    
            