import copy

def load():
    mvs, stx = [], []

    stacks_input = open('stacks.txt', 'r')
    stacks_lines = stacks_input.readlines()
    for idx, stack_line in enumerate(stacks_lines):
        initial_stack = list(stack_line.strip())
        stx.append(initial_stack)

    moves_input = open('moves.txt', 'r')
    mvs = moves_input.readlines()

    return stx, mvs


def crateMover(stx, mvs):
    stacks_9000 = stx.copy()

    for move in mvs:
        amount, from_stack,to_stack = [int(x) for x in move.split() if str.isnumeric(x)]

        for _ in range(amount):
            stacks_9000[to_stack - 1].append(stacks_9000[from_stack - 1].pop())
    
    msg_9000 = ''
    
    for s in stacks_9000:
        msg_9000 += s[-1:][0]

    return msg_9000

initial_stacks, moves = load()

print(crateMover(initial_stacks, moves))

"""
Right after completion:
- MEH! Did not feel happy about pre-formatting the input and splitting it in seperate files
- Struggled way too long with updates on (what I thought were deep copies of) sets that affected
  the copy. Turns out (I think), I should have made deep copies of the initial_stack (line 9),
  as those were still shared across stacks_9000 and stacks_9001... Cost me a few hours...
Right after seeing other people's solutions:
- Would have loved to avoid the need for arrays on elf1 and elf2
Learned:
- List/array split can also directly assing into pre-defined number of values! (line 7/8)
- Happy with the comprehension-list-filtering and splitting into the right vars on line 22!
"""