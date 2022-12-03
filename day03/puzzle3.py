input = open('input.txt', 'r')
lines = input.readlines()

def compartments(supplies):
    return supplies[slice(0, len(supplies) // 2)], supplies[slice(len(supplies) // 2, len(supplies))]

def overlap(c1, c2):
    res = []
    for i in c1:
        if i in c2 and not i in res:
            res.append(i)
    return res

def priority(c):
    item = str(c)
    p = ord(item)

    if item.islower():
        p -= 96
    elif item.isupper():
        p -= 38

    return p

def overlap2(g):
    res = []
    for i in g[0]:
        if i in g[1] and i in g[2] and not i in res:
            res.append(i)
    return res

total1, total2 = 0, 0
group = []

for idx, line in enumerate(lines):
    c1, c2 = compartments(line.strip())
    o = overlap(c1, c2)
    total1 += priority(o[0])
    group.append(line)
    if idx %3 == 2:
        o2 = overlap2(group)
        total2 += priority(o2[0])
        group = []

print(f"Answer to part 1: {total1}.\nAnswer to part 2: {total2}.")