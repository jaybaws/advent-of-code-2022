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