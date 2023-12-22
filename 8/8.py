import math

steps, nodes = open('map.txt').read().split('\n\n')

# Part 1

graph = {}
for node in nodes.split('\n'):
  source, leftright = node.split(' = ')
  left, right = leftright.split(', ')
  left, right = left[1:], right[:-1]
  graph[source] = (left, right)
  
curr = 'AAA'
num_steps = 0
while curr != 'ZZZ':
  num_steps += 1
  if steps[0] == 'L':
    curr = graph[curr][0]
  else:
    curr = graph[curr][1]
  steps = steps[1:] + steps[0]
  
print(num_steps)

# Part 2 

graph = {}
for node in nodes.split('\n'):
  source, leftright = node.split(' = ')
  left, right = leftright.split(', ')
  left, right = left[1:], right[:-1]
  graph[source] = (left, right)
  
curr = []
for key in graph.keys():
  if key[-1] == 'A':
    curr.append(key)
    
def get_period(curr, steps):
  num_steps = 0
  while not curr.endswith('Z'):
    num_steps += 1
    if steps[0] == 'L':
      curr = graph[curr][0]
    else:
      curr = graph[curr][1]
    steps = steps[1:] + steps[0]
  return num_steps
    

periods = []
for node in curr:
  periods.append(get_period(node, steps))

print(math.lcm(*periods))