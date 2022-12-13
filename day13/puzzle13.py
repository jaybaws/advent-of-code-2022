from collections.abc import Sequence
from functools import cmp_to_key

__input_file_name = 'input.txt'

def puzzle_input() -> str:
    with open(__input_file_name, 'r') as f:
        return f.read()

def is_array(x) -> bool:
    return isinstance(x, Sequence)

def is_int(x) -> bool:
    try:
        int(x)
        return True
    except:
        return False

def is_in_right_order(left, right) -> bool:
    if is_int(left) and is_int(right):
        if left < right:
            return True
        elif right < left:
            return False
        else:
            return None

    if is_int(left) and is_array(right):
        return is_in_right_order([left], right)
    elif is_int(right) and is_array(left):
        return is_in_right_order(left, [right])
        
    else:
        for idx, l in enumerate(left):
            try:
                r = right[idx]
                right_order = is_in_right_order(l, r)
                if right_order is None:
                    continue
                else:
                    return right_order
            except IndexError:
                continue

        if len(left) < len(right):
            return True
        elif len(right) < len(left):
            return False
        else:
            return None
   

def answer1() -> int:
    index, indices = 0, []
    packet_pairs = [pair.split() for pair in puzzle_input().split('\n\n')]

    for p1, p2 in packet_pairs:
        index += 1

        left, right = eval(p1), eval(p2)
        right_order = is_in_right_order(left, right)

        if right_order:
            indices.append(index)

    return sum(indices)


def answer2() -> int:
    div1, div2 = '[[2]]', '[[6]]'
    content = f"{div1}\n{div2}\n" + puzzle_input()
    all_packets = [packet for packet in content.replace('\n\n', '\n').splitlines()]

    def cmp_items(l: str, r: str) -> int:
        match is_in_right_order(eval(l), eval(r)):
            case True: return -1
            case False: return 1
            case None: return 0

    sorted_packets = sorted(all_packets, key=cmp_to_key(cmp_items))
    return (sorted_packets.index(div1) + 1) * (sorted_packets.index(div2) + 1)


if __name__ == '__main__':
    a1, a2 = answer1(), answer2()
    print(f"""
        Answer 1: {a1}.
        Answer 2: {a2}.
    """)


# *** Thoughts directly after completion:
# - Pretty happy!
#   - Recursing seemed like the right approach
#   - Made life easy by eval()'ing the packets directly into a var; saved a ton of parsing
#     -> don't hate the player, hate the game
#   - Wrapping the is_in_right_order function from part1 into a custom comparator was elegant

# *** Thoughts after seeing other people's solutions:
# - Not too bad!

# *** Learnings:
# - How to identify variable type (array/int)
# - Custom sorting; creating sort key from a cmp
# - Defining a custom function (callable) within a function/method