with open("Day2/input2.txt", "r") as f:
    lines = f.readlines()

def test(line):
    ascending = True if line[0] < line[1] else False
    if ascending:
        for i in range(1, len(line)):
            if not line[i] > line[i - 1]: return False
            if not 1 <= abs(line[i] - line[i - 1]) <= 3: return False
            if i == len(line) - 1: return True
    else:
        for i in range(1, len(line)):
            if not line[i] < line[i - 1]: return False
            if not 1 <= abs(line[i] - line[i - 1]) <= 3: return False
            if i == len(line) - 1: return True
    return False

lines = [list(map(int, i.split())) for i in lines]

total = 0

for line in lines:
    if test(line):
        total += 1
    else:
        for el in range(len(line)):
            lineCopy = line[:el] + line[el+1:]
            if test(lineCopy):
                total += 1
                break

print(total)
