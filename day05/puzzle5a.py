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
        items = move.split()
        amount = int(items[1])
        from_stack = int(items[3])
        to_stack = int(items[5])
        for _ in range(amount):
            stacks_9000[to_stack - 1].append(stacks_9000[from_stack - 1].pop())
    
    msg_9000 = ''
    
    for s in stacks_9000:
        msg_9000 += s[-1:][0]

    return msg_9000

initial_stacks, moves = load()

print(crateMover(initial_stacks, moves))