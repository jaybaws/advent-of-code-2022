from typing import Tuple, List
import numpy as np

__input_file_name = 'input.txt'

def load_input() -> List[List[int]]:
    def func(s:str) -> Tuple[int, int]:
        x, y = s.split(',')
        return int(x), int(y)

    with open(__input_file_name, 'r') as f:
        file_content = f.read()
    return [ list(map(func, rock.split(' -> '))) for rock in file_content.splitlines() ]

def generate_cave(rocks_list: List[List[int]], part: int):
    depth = max([ y for rocks in rocks_list for x,y in rocks]) + 1 + (part - 1)
    width = max([ x for rocks in rocks_list for x,y in rocks]) + 1 + (depth + 1)

    cave = np.matrix(np.zeros(shape=(depth, width)), dtype=int)

    for rocks in rocks_list:
        for i in range(len(rocks) - 1):
            a_x, a_y = rocks[i]
            b_x, b_y = rocks[i + 1]
                
            dx, dy = b_x - a_x, b_y - a_y 
            d = max(abs(dx), abs(dy))
            dx, dy = dx//d, dy//d            

            for i in range(d + 1):
                nx, ny = a_x + (i*dx), a_y + (i*dy)
                cave[ny, nx] = 8

    return cave, width, depth

def answer(part:int) -> int:
    cave, width, depth = generate_cave(load_input(), part)

    i = 0
    while True:
        i += 1
        at_rest = False
        x, y = 500, 0
        while not at_rest:
            # Check exit conditions first!
            if cave[0, 500] == 1:  # WE FLOODED!
                return i - 1
            elif y+1 == depth:  # vertical oob
                match part:
                    case 1:  # Stuff 'falls into the abyss'. Return the amount of particles that led up to this.
                        return i - 1
                    case 2:  # Consider the bottom to be a physical boundary. Then there is no way to go diagonally left or right, and this particle falls to rest.
                        cave[y, x] = 1
                        at_rest = True

            if not at_rest:
                if cave[y + 1, x] == 0:
                    y += 1
                else:
                    if (x-1>0) and cave[y+1, x-1] == 0:  # left is not oob and free
                        x -= 1
                        y += 1
                    elif (x+1<width) and cave[y+1, x+1] == 0:  # right is not oob and free
                        x += 1
                        y += 1
                    else:  # oob or not free --> to rest!
                        cave[y, x] = 1
                        at_rest = True


if __name__ == '__main__':
    print(f"Answer 1: {answer(1)}")
    print(f"Answer 1: {answer(2)}")

# *** Thoughts directly after completion:
# - Took too long...
#   - Shouldn't have used NumPy. Instead, just render a list of 'obstructed coordinates' (based on the
#     obstructed lines from the puzzle input), and 'flood-fill' that list...
#     -> This would have avoided the issues of (no be able to) spilling over horizontally (caused 
#        index-oob with the matrix...)
#   - I got lucky that my test-input wasn't close to the x-axis, so particles could spill over to the left
#     before running into negative-x coordinates (which would not have fitted in the matrix)... 
#     -> I was lucky that 'widening' the matrix horizonally worked with my test-input ...

# *** Thoughts after seeing other people's solutions:
# - Affraid to look; I will cry if I do :)

# *** Learnings:
# - Look up flood-fill algorith first between building crap right away...
#   -> Should have used a Set of coordinates or something.
# - Don't use NumPy because it looks fancy :)
# ==> Your success does indeed really depend on the data-structure you choose :)