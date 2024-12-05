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


tot = 0

for pages in part2:
    seen = set([])
    NO = False
    print(pages)
    for page in pages:
        prevs = part1[page]
        for prev in prevs:
            if prev in seen:
                NO = True
                break
        seen.add(page)
    if not NO:
        tot += get_middle(pages)

print(tot)
