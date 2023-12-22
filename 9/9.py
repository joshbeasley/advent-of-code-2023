file = open('oasis.txt')
lines = file.readlines()

for line in lines:
    values = list(map(int, line.split()))
    print(values)