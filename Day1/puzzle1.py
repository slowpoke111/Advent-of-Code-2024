right,left = [],[]

with open('Day1/input1.txt') as f:
    lines = f.readlines()
    for i,el in enumerate(lines[:-1]):
        x,y = list(map(int,el.split()))
        left.append(x)
        right.append(y)

left.sort()
right.sort()

sum = 0
for i in zip(left,right):
    sum +=abs(i[0]-i[1])

print(sum)