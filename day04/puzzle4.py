input = open('input.txt', 'r')
lines = input.readlines()

total1, total2 = 0, 0

for line in lines:
    range1, range2 = line.strip().split(',')
    elf1, elf2 = range1.split('-'), range2.split('-')
   
    a, b, c, d = int(elf1[0]), int(elf1[1]), int(elf2[0]), int(elf2[1])

    set1 = set(range(a, b + 1))
    set2 = set(range(c, d + 1))
   
    if (set1.issuperset(set2) or set2.issuperset(set1)):
        total1 += 1
    
    if (len(set1.intersection(set2)) > 0):
        total2 += 1

print(f"""Solutions for puzzle of day 4:
- Answer one: {total1}.
- Answer two: {total2}.
""")


"""
Right after completion:
- Pretty happy with the code
Right after seeing other people's solutions:
- Would have loved to avoid the need for arrays on elf1 and elf2
Learned:
- List/array split can also directly assing into pre-defined number of values! (line 7/8)
"""