import re

file = open("engine.txt", "r")
lines = file.readlines()

engine = []

for line in lines:
  split_line = [*line]
  if split_line[-1] == '\n':
    engine.append(split_line[:-1])
  else:
    engine.append(split_line)

locations = {}
parts = set()

for i in range(len(lines)):
  split_line = re.split(r'\D+', lines[i])
  for c in split_line:
    if c.isdigit():
      occurences = [i.start() for i in re.finditer(c, lines[i])]
      final_idx = occurences[0]
      for idx in occurences:
        if (i, idx) in locations:
          continue
        else:
          final_idx = idx
          break
      for j in range(len(c)):
        locations[(i, final_idx + j)] = int(c)
      parts.add(int(c))

total = 0

for i in range(len(engine)):
  for j in range(len(engine[0])):
    if not engine[i][j].isdigit() and engine[i][j] != '.':
      if i+1 < len(engine) and engine[i+1][j].isdigit() and locations[(i+1,j)] in parts:
        total += locations[(i+1,j)]
        parts.remove(locations[(i+1,j)])
      if i+1 < len(engine) and j+1 < len(engine[0]) and engine[i+1][j+1].isdigit() and locations[(i+1,j+1)] in parts:
        total += locations[(i+1,j+1)]
        parts.remove(locations[(i+1,j+1)])
      if i+1 < len(engine) and j-1 >= 0 and engine[i+1][j-1].isdigit() and locations[(i+1,j-1)] in parts:
        total += locations[(i+1,j-1)]
        parts.remove(locations[(i+1,j-1)])
      if j+1 < len(engine[0]) and engine[i][j+1].isdigit() and locations[(i,j+1)] in parts:
        total += locations[(i,j+1)]
        parts.remove(locations[(i,j+1)])
      if j+1 < len(engine[0]) and i-1 >= 0 and engine[i-1][j+1].isdigit() and locations[(i-1,j+1)] in parts:
        total += locations[(i-1,j+1)]
        parts.remove(locations[(i-1,j+1)])
      if j-1 >= 0 and engine[i][j-1].isdigit() and locations[(i,j-1)] in parts:
        total += locations[(i,j-1)]
        parts.remove(locations[(i,j-1)])
      if j-1 >= 0 and i-1 >= 0 and engine[i-1][j-1].isdigit() and locations[(i-1,j-1)] in parts:
        total += locations[(i-1,j-1)]
        parts.remove(locations[(i-1,j-1)])
      if i-1 >= 0 and engine[i-1][j].isdigit() and locations[(i-1,j)] in parts:
        total += locations[(i-1,j)]
        parts.remove(locations[(i-1,j)])
print(total)
      

