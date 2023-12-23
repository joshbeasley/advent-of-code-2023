def find_mirror(grid):
    for i in range(1, len(grid)):
        above = grid[:i][::-1]
        below = grid[i:]
        
        above = above[:len(below)]
        below = below[:len(above)]
        
        if above == below:
            return i
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
    
    

    