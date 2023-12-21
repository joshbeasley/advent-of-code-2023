file = open('hands.txt')

vals = {'T':'A', 'J':'B', 'Q':'C', 'K':'D', 'A':'E'}

scores = []
plays = []
for line in file.readlines():
  hand, bid = line.split()
  plays.append((hand, int(bid)))
  counts = {}
  score = -1
  for card in hand:
    if card in counts:
      counts[card] += 1
    else:
      counts[card] = 1
  if len(counts) == 1:
    score = 7
  elif len(counts) == 2:
    if 2 in counts.values():
      score = 5
    else:
      score = 6
  elif len(counts) == 3:
    if 3 in counts.values():
      score = 4
    else:
      score = 3
  elif len(counts) == 4:
    score = 2
  else:
    score = 1
    
  scores.append((score, [vals.get(char, char) for char in hand]))
  
print(scores)
  
plays  = [x for _, x in sorted(zip(scores, plays))]

total = 0
for rank, (hand, bid) in enumerate(plays):
  total += (rank + 1) * bid

print(total)
