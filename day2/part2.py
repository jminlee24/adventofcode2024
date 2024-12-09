data = []


def is_safe(line):
    incr = False
    decr = False
    safe = True

    for i in range(len(line) - 1):
        if line[i] < line[i + 1]:
            incr = True
        elif line[i] > line[i + 1]:
            decr = True
        else:
            safe = False
        if abs(line[i] - line[i + 1]) > 3 or (decr and incr):
            safe = False
    return safe


with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        vals = line.split(" ")
        vals = list(map(lambda x: int(x.strip()), vals))
        data.append(vals)

safe_count = 0

for line in data:
    if is_safe(line):
        safe_count += 1
    else:
        for i in range(len(line)):
            if is_safe(line[0:i] + line[i+1:]):
                safe_count += 1
                break
print(safe_count)
