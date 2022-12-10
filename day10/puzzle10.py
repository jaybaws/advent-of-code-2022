from textwrap import wrap

cycles = [20, 60, 100, 140, 180, 220]
cycle_cost = { 'addx': 2, 'noop': 1 }

with open('input.txt', 'r') as f:
    ops = [(cycle_cost[l[:4]], int(l[5:])) for l in f.read().replace("noop", "noop 0").splitlines()]
    # Creates list of tuples that describe the operation: (operation-cycle-cost, x-value-increment)

def x_value_at(cycle: int) -> int:
    return 1 + sum([ops[i][1] for i in range(len(ops)) if sum([op[0] for op in ops[:i + 1]]) <= (cycle - 1)])

def x_value_after(cycle: int) -> int:
    return x_value_at(cycle + 1)

def signal_strength_at(cycle: int) -> int:
    return cycle * x_value_at(cycle)

def answer1() -> int:
    return sum(signal_strength_at(cycle) for cycle in cycles)

def answer2() -> str:
    crt = ""
    for cycle in range(1, 240 + 1):
        x = x_value_after(cycle - 1)
        crt += "#" if (cycle - 1) % 40 in (x - 1, x, x + 1) else "."
    return "\n".join(wrap(crt, 40))

print(f"""
    Answer 1: {answer1()}
    Answer 2:

{answer2()}

    Yay!
""")

"""
Right after completion:
- Felt smart about loading/coercing the input data
  - string-replacing the zero cost of noop into the input, before translating using a dictionary.
- Made a more functional approach to determining the signal strength and value of x
  - able to do it on one line
- Not really happy that I kept `ops` a global variable, but 'hey, it works!'
Right after seeing other people's solutions:
- This time, procedural might have actually been easier :-D (as proven by part 2)
- dictionaries
Learned:
- nested and conditional list comprehension (line 7 and 10)
- conditional value assignment (var = 'someval' if (condition) else 'somethingelse')
- textwrap module
- joining a list of string into an uber-string (line 27)
"""