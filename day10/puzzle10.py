from textwrap import wrap

cycles = [20, 60, 100, 140, 180, 220]
cycle_cost = { 'addx': 2, 'noop': 1 }

with open('input.txt', 'r') as f:
    ops = [(cycle_cost[l[:4]], int(l[5:])) for l in f.read().replace("noop", "noop 0").splitlines()]
    # Creates list of tuples that describe the operation: (operation-cycle-cost, x-value-increment)

def x_value_at(cycle: int) -> int:
    return 1 + sum([ops[i][1] for i in range(len(ops)) if sum([op[0] for op in ops[:i + 1]]) <= (cycle - 1)])

def signal_strength_at(cycle: int) -> int:
    return cycle * x_value_at(cycle)

def answer1() -> int:
    return sum(signal_strength_at(cycle) for cycle in cycles)

def answer2() -> str:
    crt = ""
    for cycle in range(1, 240 + 1):
        x = x_value_at(cycle)
        crt += "#" if (cycle - 1) % 40 in (x - 1, x, x + 1) else "."
    return "\n".join(wrap(crt, 40))

print(f"""
    Answer 1: {answer1()}
    Answer 2:

{answer2()}

    Yay!
""")

# *** Thoughts directly after completion:
# - Generally really happy, although it took quite some effort (multiple hours)
# - Felt smart about loading/coercing the input data
#   - string-replacing the zero cost of noop into the input, before translating using a dictionary. (line 7)
# - Made a more functional approach to determining the signal strength and value of x at a given cycle
#   - Able to do it on one line
# - Not really happy that I kept `ops` a global variable, but 'hey, it works!' :D

# *** Thoughts after seeing other people's solutions:
# - My sense for style sucks ;-) This time, procedural might have actually been easier :D (as proven by part 2)

# *** Learnings:
# - creating contexts using `with`, which eases error handling and cleanup (auto closing of file handle) (line 6)
# - nested and conditional list comprehension (line 7 and 11)
# - conditional value assignment (var = 'someval' if (condition) else 'somethingelse') (line 23)
# - textwrap module (line 24)
# - joining a list of string into an uber-string (line 24)