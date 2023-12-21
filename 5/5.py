# file = open("mapping.txt", "r")
# lines = file.readlines()

# seeds = [int(i) for i in lines[0].split(':')[1].split()]

# mapping_groups = []
# current_group = []
# i = 1
# while i < len(lines):
#   if lines[i][0] == '\n':
#     mapping_groups.append(current_group)
#     current_group = []
#     i += 2
#     continue
#   current_group.append([int(i) for i in lines[i].split()])
#   i += 1

# mapping_groups = mapping_groups[1:]

# def in_range(mapping, source):
#   if source >= mapping[1] and source < mapping[1] + mapping[2]:
#     return True
#   return False

# def single_mapping(mapping, source):
#   return source - mapping[1] + mapping[0]

# def execute_mapping(group, source):
#   destination = -1
#   for mapping in group:
#     if in_range(mapping, source):
#       destination = single_mapping(mapping, source)
#       break
#   else:
#     return source
#   return destination

# locations = []
# for seed in seeds:
#   destination = seed
#   for group in mapping_groups:
#     destination = execute_mapping(group, destination)
#   locations.append(destination)

# print(min(locations))

seeds, *blocks = open('mapping.txt').read().split('\n\n')
seeds = list(map(int, seeds.split(':')[1].split()))
new_seeds = []
for i in range(0, len(seeds) - 1, 2):
  new_seeds.append((seeds[i], seeds[i] + seeds[i+1]))

seeds = new_seeds

for block in blocks:
  ranges = []
  for line in block.splitlines()[1:]:
    ranges.append(list(map(int, line.split())))
  locations = []
  while len(seeds) > 0:
    s, e = seeds.pop()
    for a, b, c in ranges:
      os = max(s, b)
      oe = min(e, b + c)
      if os < oe:
        locations.append((os - b + a, oe - b + a))
        if os > s:
          seeds.append((s, os))
        if e > oe:
          seeds.append((oe, e))
        break
    else:
      locations.append((s, e))
  seeds = locations

print(min(locations)[0])
