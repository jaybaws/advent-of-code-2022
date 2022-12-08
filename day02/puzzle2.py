scores_by_exact_play = [ ('A X', 1 + 3), ('A Y', 2 + 6), ('A Z', 3 + 0), ('B X', 1 + 0), ('B Y', 2 + 3), ('B Z', 3 + 6), ('C X', 1 + 6), ('C Y', 2 + 0), ('C Z', 3 + 3) ]
scores_by_desired_outcome = [ ('A X', 0 + 3), ('A Y', 3 + 1), ('A Z', 6 + 2), ('B X', 0 + 1), ('B Y', 3 + 2), ('B Z', 6 + 3), ('C X', 0 + 2), ('C Y', 3 + 3), ('C Z', 6 + 1) ]

def score(round, input):
    return list(filter(lambda tup: tup[0] == round, input))[0][1]

input = open('input.txt', 'r')
lines = input.readlines()

total_score_1, total_score_2 = 0, 0

for line in lines:
    play = line.strip()
    total_score_1 += score(play, scores_by_exact_play)
    total_score_2 += score(play, scores_by_desired_outcome)

print(f"{total_score_1}, {total_score_2}")

"""
Right after completion:
- HA! Feeling smart by pre-determining all the scores/desired actions. Should make processing fast/efficient
Right after seeing other people's solutions:
- Could/should have used a dict instead of tuples. Probably easier to filter later on! DANG IT!
"""