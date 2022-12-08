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
    stacks_9001 = stx.copy()

    for move in mvs:
        items = move.split()
        amount = int(items[1])
        from_stack = int(items[3])
        to_stack = int(items[5])

        tmp_stack = []
        for _ in range(amount):
            tmp_stack.append(stacks_9001[from_stack - 1].pop())
        tmp_stack.reverse()
        stacks_9001[to_stack - 1].extend(tmp_stack)
    
    msg_9001 = ''
    
    for s in stacks_9001:
        msg_9001 += s[-1:][0]

    return msg_9001

initial_stacks, moves = load()

print(crateMover(initial_stacks, moves))

"""
Right after completion:
- Wasn't that hard. Understoond quickly I had to reverse the popped elements.
- Still not happy that I could not get this to work in one method (working on
  two deep-copied sets...)
Right after seeing other people's solutions:
- 
Learned:
- 
"""