with open("2024/Day2/input2.txt","r") as f:
    lines = f.readlines()

lines = [list(map(int,i.split())) for i in lines]

total = 0

for line in lines:
    ascending = True if line[0]<line[1] else False 
    
    if ascending:
        for i in range(1,len(line)):
            if not line[i]>line[i-1]: break
            if not 1<=abs(line[i]-line[i-1])<=3: break
            if i==len(line)-1: total+=1
    else:
        for i in range(1,len(line)):
            if not line[i]<line[i-1]: break
            if not 1<=abs(line[i]-line[i-1])<=3: break
            if i==len(line)-1: total+=1

print(total)