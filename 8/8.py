steps, nodes = open('map.txt').read().split('\n\n')

# class Node:
#   def __init__(self, source, left, right):
#     self.source = source
#     self.left = left
#     self.right = right

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
  
  