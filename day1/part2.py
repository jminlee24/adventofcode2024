data1 = []
data2 = {}

with open("input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        l1, l2 = line.strip().split("   ")
        l1 = int(l1)
        l2 = int(l2)
        data1.append(l1)
        if l2 in data2:
            data2[l2] += 1
        else:
            data2[l2] = 1
tot = 0
for d in data1:
    if d in data2:
        tot += d * data2[d]

print(tot)
