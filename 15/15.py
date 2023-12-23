steps = open('steps.txt').read().split(',')

def hash(s):
    curr = 0
    for char in s:
        curr += ord(char)
        curr *= 17
        curr %= 256
    return curr

total = 0
for step in steps:
    total += hash(step)
print(total)
        