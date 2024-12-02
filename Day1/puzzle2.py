right,left = [],[]

with open('Day1/input1.txt') as f:
    lines = f.readlines()
    for i,el in enumerate(lines[:-1]):
        x,y = list(map(int,el.split()))
        left.append(x)
        right.append(y)

appearanceInRight = {}
for i in right:
    if i in appearanceInRight:
        appearanceInRight[i]+=1
    else:
        appearanceInRight[i]=1

total = 0

for i in left:
    try:
        factor = appearanceInRight[i]
    except Exception:
        factor=0

    total+=i*factor

print(total)