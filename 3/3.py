import re

grid = open('engine.txt').read().splitlines()
cs = set()

ratios = []
for r, row in enumerate(grid):
  for c, ch in enumerate(row):
    if ch == "*":
      ratio = set()
      for cr in [r - 1, r, r + 1]:
        for cc in [c - 1, c, c + 1]:
          if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
            continue
          while cc > 0 and grid[cr][cc - 1].isdigit():
            cc -= 1
          cs.add((cr, cc))
          ratio.add((cr, cc))
      ratios.append(ratio)

total = 0
for ratio in ratios:
  if len(ratio) == 2:
    product = 1
    for r, c in ratio:
      num = ''
      while c < len(grid[r]) and grid[r][c].isdigit():
        num += grid[r][c]
        c += 1
      product *= int(num)
    total += product

print(total)

# ns = []
# for r, c in cs:
#   num = ''
#   while c < len(grid[r]) and grid[r][c].isdigit():
#     num += grid[r][c]
#     c += 1
#   ns.append(int(num))

# print(sum(ns))
