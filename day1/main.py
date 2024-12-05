data1 = []
data2 = []

tot = 0

with open("input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        l1, l2 = line.strip().split("   ")
        l1 = int(l1)
        l2 = int(l2)
        data1.append(l1)
        data2.append(l2)


data1 = sorted(data1)
data2 = sorted(data2)

for i in range(len(data1)):
    tot += abs(data1[i] - data2[i])

print(tot)
