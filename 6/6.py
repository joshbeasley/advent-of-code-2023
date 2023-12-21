# Part 1
times, distances = open('races.txt').read().split('\n')

times = list(map(int, times.split(':')[1].split()))
distances = list(map(int, distances.split(':')[1].split()))

total = 1
for idx, time in enumerate(times):
  records = 0
  for speed in range(1, time-1):
    if speed * (time - speed) > distances[idx]:
      records += 1
  total *= records
  
print(total)
