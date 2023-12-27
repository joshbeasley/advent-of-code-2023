lines = open('grid.txt').read().splitlines()

grid = []
for _ in range(100):
    row = []
    for _ in range(100):
        row.append('.')
    grid.append(row)

start 
for line in lines:
    direction, distance, color = line.split()
    