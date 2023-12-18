file = open("cubes.txt", "r")
lines = file.readlines()

record = []

for line in lines:
  record.append([])
  game_id, games = line.split(':')

  games = games.split(';')
  for game in games:
    red, green, blue = -1, -1, -1
    red_idx = game.find('red')
    green_idx = game.find('green')
    blue_idx = game.find('blue')
    if red_idx != -1:
      red = int(game[red_idx-3:red_idx-1]) if game[red_idx-3].isdigit() else int(game[red_idx-2])
    if green_idx != -1:
      green = int(game[green_idx-3:green_idx-1]) if game[green_idx-3].isdigit() else int(game[green_idx-2])
    if blue_idx != -1:
      blue = int(game[blue_idx-3:blue_idx-1]) if game[blue_idx-3].isdigit() else int(game[blue_idx-2])
    record[-1].append((red, green, blue))

# Part 1

# red_max, green_max, blue_max = 12, 13, 14
# total = 0
# for i in range(len(record)):
#   total += i + 1
#   for (red, green, blue) in record[i]:
#     if red > red_max or green > green_max or blue > blue_max:
#       total -= i + 1
#       break
# print(total)

# Part 2
total = 0
for game in record:
  red = max([draw[0] for draw in game if draw[0] != -1 ])
  green = max([draw[1] for draw in game if draw[1] != -1])
  blue = max([draw[2] for draw in game if draw[2] != -1])
  total += red * green * blue
print(total)

