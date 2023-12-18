file = open("cards.txt", "r")
lines = file.readlines()

winners, mine = [], []
for line in lines:
  w, m = line.split(':')[1].split('|')
  winners.append(w.split())
  mine.append(m.split())

total = 0
for i in range(len(winners)):
  winnings = 0
  for j in range(len(mine[i])):
    if mine[i][j] in winners[i]:
      if winnings == 0:
        winnings += 1
      else:
        winnings *= 2
  total += winnings

print(total)