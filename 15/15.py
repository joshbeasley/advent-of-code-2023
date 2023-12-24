steps = open('steps.txt').read().split(',')

boxes = {}
for i in range(256):
    boxes[i] = []

def hash(s):
    curr = 0
    for char in s:
        curr += ord(char)
        curr *= 17
        curr %= 256
    return curr

total = 0
for step in steps:
    label = None
    lense = None
    if step[-1] == '-':
        label = step[:-1]
    else:
        label = step[:-2]
        lense = step[-1]
    box = hash(label)

    if lense:
        label_idx = None
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == label:
                label_idx = i
                break
        if label_idx is not None:
            boxes[box][label_idx][1] = lense
        else:
            boxes[box].append([label, lense])
    else:
        label_idx = None
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == label:
                label_idx = i
                break
        if label_idx is not None:
            test = boxes[box].pop(label_idx)

total = 0
for i in range(255):
    if len(boxes[i]) > 0:
        for j in range(len(boxes[i])):
            total += (i + 1) * (j + 1) * int(boxes[i][j][1])
print(total)
                
        