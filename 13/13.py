def find_mirror(grid):
    for i in range(1, len(grid)):
        above = grid[:i][::-1]
        below = grid[i:]
        
        above = above[:len(below)]
        below = below[:len(above)]
        
        mismatches = 0
        for r in range(len(above)):
            for c in range(len(above[0])):
                if above[r][c] != below[r][c]:
                    mismatches += 1
        
        if mismatches == 1:
            return i
        # if above == below:
        #     return i
    return 0

total = 0
for block in open('mirrors.txt').read().split('\n\n'):
    
    grid = block.splitlines()   
    row = find_mirror(grid)
    
    total += row * 100
    
    grid = list(zip(*grid))
    col = find_mirror(grid)
    total += col

print(total)
    
    

    