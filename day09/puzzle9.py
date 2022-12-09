from typing import Tuple, List


def to_displacements(move: str) -> (Tuple[int, int, int]):
    direction, distance = move.split(' ')
    match direction:
        case 'U': return ( 0,  1, int(distance))
        case 'D': return ( 0, -1, int(distance))
        case 'L': return (-1,  0, int(distance))
        case 'R': return ( 1,  0, int(distance))
        case _:   return ( 0,  0, 0)


def halve(x: int) -> int:
    if abs(x) > 1: 
        return x//2
    else:
        return x


moves = list(map(to_displacements, open('input.txt', 'r').read().splitlines()))


class Rope:
    knot_positions: List[List[Tuple[int, int]]]

    def __init__(self, amount_of_knots: int):
        self.knot_positions = list(list(({})))
        for _ in range(amount_of_knots):
            self.knot_positions.append(list({(0, 0)}))

    def positions_visisted_by_tail(self, moves: Tuple[int, int, int]) -> int:
        for (x, y, d) in moves:  # Process them move-by-move
            for _ in range(d):  # Process each move step-by-step
                (head_x, head_y) = self.knot_positions[0][-1]  # Current position of the HEAD is the last position in the list of the first knot
                self.knot_positions[0].append((head_x + x, head_y + y))  # Add the new position to the list
                
                for rope in range(1, len(self.knot_positions)):  # Process each subsequent (non-HEAD) knot
                    (rope_x, rope_y) = self.knot_positions[rope][-1]  # Determine it's position
                    (prev_rope_x, prev_rope_y) = self.knot_positions[rope - 1][-1]  # Determine the position of it's preceeding knot

                    (dx, dy) = (prev_rope_x - rope_x, prev_rope_y - rope_y)  # Determine the disposition between this knot and it's preceeding knot
                    if abs(dx) > 1 or abs(dy) > 1:  # When this knot is not adjacent to it's preceeding knot ... 
                        ox, oy = halve(dx), halve(dy)  # Determine how much it must move, and ...
                        self.knot_positions[rope].append((rope_x + ox, rope_y + oy))  # Add it's new position

        return len(set(self.knot_positions[-1]))


a1 = Rope(2).positions_visisted_by_tail(moves)
a2 = Rope(10).positions_visisted_by_tail(moves)

assert(a1 == 6498)
assert(a2 == 2531)

print(f"""
    Answer one: {a1}.
    Answer two: {a2}.
""")

"""
Right after completion:
- More consise loading of the input (happy with map function)
- Easy to make on generic function
Right after seeing other people's solutions:
- 
Learned:
- tuples
  - how to type-hint tuples in functions
- match cases
- map() function
- difference in division between / and //
- difference between class variables and instance variables
"""