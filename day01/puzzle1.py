input = open('input.txt', 'r')
lines = input.readlines()

calories = 0
maxima = []

for line in lines:
    if line == "\n":
        maxima.append(calories)
        calories = 0
    else:
        calories += int(line)

print(max(maxima))

maxima.sort(reverse=True)
print(sum(maxima[:3]))

"""
Right after completion:
- Pretty happy with the code
Right after seeing other people's solutions:
- 'too procederural'...
  - could have used list comprehension
  - could have split on \n\n first, creating a list of list-of-calaries
"""