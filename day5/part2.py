part1 = {}
part2 = []
S = False

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line == "\n":
            S = True
        elif S:
            part2.append(line.strip().split(","))
        else:
            prev, after = line.strip().split("|")
            if prev in part1:
                part1[prev].append(after)
            else:
                part1[prev] = [after]


def get_middle(lst: list):
    return int(lst[len(lst) // 2])


def swap(lst, x1, x2):
    temp = lst[x1]
    lst[x1] = lst[x2]
    lst[x2] = temp


tot = 0

for pages in part2:
    seen = {}
    for i, page in enumerate(pages):
        prevs = part1[page]
        seen[page] = i
        for prev in prevs:
            if prev in seen:
                swap(pages, i, seen[prev])
    tot += get_middle(pages)

print(tot)
