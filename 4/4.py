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

copies = [1] * len(winners)
for i, wins in enumerate(num_win):
  for j in range(i + 1, i + wins + 1):
    copies[j] += copies[i] 
print(copies)
print(sum(copies))

