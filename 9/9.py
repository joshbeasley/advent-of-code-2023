file = open('oasis.txt')
lines = file.readlines()

def generate_differences(values):
    diffs = []
    diffs.append(values)
    while set(values) != set([0]):
        diff = []
        for i in range(1, len(values)):
            diff.append(values[i] - values[i-1])
        diffs.append(diff)
        values = diff
    return diffs

def extrapolate(diffs):
    diffs.reverse()
    for i in range(1, len(diffs)):
        diffs[i].append(diffs[i][-1] + diffs[i-1][-1])
    return diffs

total = 0
for line in lines:
    values = list(map(int, line.split()))
    diffs = generate_differences(values)
    extrapolation = extrapolate(diffs)
    total += extrapolation[-1][-1]
    
print(total)
    