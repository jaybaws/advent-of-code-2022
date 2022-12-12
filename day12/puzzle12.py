from io import StringIO
from typing import Tuple
import numpy as np

def determine_shortest_paths_to_end(initial_grid):
    start_row, start_col = None, None
    total_rows, total_cols = initial_grid.shape
    grid = np.copy(initial_grid)

    something_changed = True
    while something_changed:
        something_changed = False
        for r in range(total_rows):
            for c in range(total_cols):
                cur_letter, cur_h, cur_d = grid[r,c]
                if cur_letter == 'S': start_row, start_col = r, c
                if cur_d is None and cur_letter == 'E': grid[r,c], something_changed = (cur_letter, cur_h, 0), True

                for (dr,dc) in [(-1,0), (0,-1), (1,0), (0,1)]:  # Try all horizontal and vertical neighbours
                    if (r+dr >= 0) and (c+dc >= 0) and (r+dr < total_rows) and (c+dc < total_cols):  # Avoid testing non-existent/out-of-bound
                        _, nbr_h, nbr_d = grid[r+dr, c+dc]
                        if (nbr_h <= cur_h) or (nbr_h == cur_h + 1):  # Can it reach it's neighbour?
                            if nbr_d is not None and (cur_d is None or (cur_d > nbr_d + 1)):
                                cur_d = nbr_d + 1
                                grid[r,c] = (cur_letter, cur_h, cur_d)
                                something_changed = True

    return grid, start_row, start_col

def converter(c: str) -> Tuple[str, int, int]:
    """Create tuples of (height-letter, height-numeric, distance-to-end). distance-to-end defaults at None."""
    match c:
        case b'S': return (chr(ord(c)), (ord('a') - ord('a')), None)
        case b'E': return (chr(ord(c)), (ord('z') - ord('a')), None)
        case _   : return (chr(ord(c)), abs(ord(c) - ord('a')), None)

def answer(fileName: str) -> Tuple[int, int]:
    with open(fileName, 'r') as f:
        grid = np.asmatrix(np.loadtxt(StringIO(f.read().replace("", " ")), dtype="object", converters=converter))
        max_r, max_c = grid.shape
        lowest_starting_points = []

    shortest_paths_to_end, start_row, start_col = determine_shortest_paths_to_end(grid)

    for r in range(max_r): 
        for c in range(max_c):
            l, h, d = shortest_paths_to_end[r, c]
            if l == 'a' and d is not None:
                lowest_starting_points.append(d) 

    return shortest_paths_to_end[start_row,start_col][2], min(lowest_starting_points)

if __name__ == '__main__':
    a1, a2 = answer('input.txt')
    print(f"""
        Answer 1: {a1}.
        Answer 2: {a2}.
    """)

# *** Thoughts directly after completion:
# - FUCK-ME-DEAD
#   - I was off-by-1 for half the day...
#     -> Attempted to (optimistically) check all neighbours (up/down/left/right) and assumed some sort of
#        OutOfBounds exception would be thrown, which I thought I neutralized. However, NumPy just returns None
#        if you ask for crap :)
# - Might not have needed NumPy in this case, but happy I tried :)
# - Found a relatively short/quick/readable way to parse the input into a NumPy matrix
# - Could not find the energy to optimize answer 2. This should be doable in a more elegant
#   filter or comprehension list, but I'm too tired...

# *** Thoughts after seeing other people's solutions:
# - Should have maybe looked for Dijkstra's algorithm first, instead of building my own :)
# - Could have used breadth-first-search. Did not think of that...

# *** Learnings:
# - NumPy matrix, and loading from text
# - Bastiaans' shortest-path-yet-not-so-fast algorithm :D