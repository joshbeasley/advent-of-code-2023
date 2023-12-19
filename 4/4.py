from math import log2

file = open("cards.txt", "r")
lines = file.readlines()

winners, mine = [], []
for line in lines:
  w, m = line.split(':')[1].split('|')
  winners.append(w.split())
  mine.append(m.split())

total = 0
record = {}
num_win = []
for i in range(len(winners)):
  winnings = 0
  num_winners = 0
  for j in range(len(mine[i])):
    if mine[i][j] in winners[i]:
      winnings = 2**num_winners
      num_winners += 1 
  record[i] = winnings
  num_win.append(num_winners)
print(sum(record.values()))
print(num_win)

total = len(winners)
print(total)

def process_scratchcard(i):
  if num_win[i] == 0:
    return 0
  total = num_win[i]
  for j in range(i+1, total+1):
    total += process_scratchcard(j)
  return total

for i in range(len(num_win)):
  total += process_scratchcard(i)

print(total)


# i = 4, len(record) = 5, num_winner = 3
