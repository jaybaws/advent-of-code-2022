from io import StringIO
from typing import Tuple
import numpy as np

def shortest_paths_to_E(initial_grid):
    grid = np.copy(initial_grid)
    total_rows, total_cols = initial_grid.shape
    start_row, start_col = None, None

    start_found = False
    something_changed = True
    while something_changed:
        something_changed = False
        for r in range(total_rows):
            for c in range(total_cols):
                cur_letter, cur_h, cur_d = grid[r, c]
                if not start_found and cur_letter == 'S':
                    start_row = r
                    start_col = c
                    start_found = True

                if cur_d is None and cur_letter == 'E':
                    cur_d = 0
                    grid[r, c] = (cur_letter, cur_h, cur_d)
                    something_changed = True

                for (dr, dc) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    if (r+dr >= 0) and (c + dc >= 0) and (r+dr < total_rows) and (c+dc < total_cols):
                        nbr_letter, nbr_h, nbr_d = grid[r+dr, c+dc]
                        can_reach_nbr = (nbr_h <= cur_h) or (nbr_h == cur_h + 1)
                        if can_reach_nbr:
                            if nbr_d is not None and (cur_d is None or (cur_d > nbr_d + 1)):
                                cur_d = nbr_d + 1
                                grid[r, c] = (cur_letter, cur_h, cur_d)
                                something_changed = True
                    else:
                        pass

    return grid, start_row, start_col

def converter(char: str) -> Tuple[str, int, int]:
    match char:
        case b'S': height = (ord('a') - ord('a'))
        case b'E': height = (ord('z') - ord('a'))
        case _   : height = abs(ord(char) - ord('a'))
    
    return (chr(ord(char)), height, None)

def answer1(fileName: str) -> int:
    with open(fileName, 'r') as f:
        txt = f.read().replace("", " ")

    c = StringIO(txt)
    grid = np.asmatrix(np.loadtxt(c, dtype="object", converters=converter))
    paths, sr, sc = shortest_paths_to_E(grid)

    max_r, max_c = paths.shape
    starting_points = []
    for r in range(max_r): 
        for c in range(max_c):
            l, h, d = paths[r, c]
            if l == 'a' and d is not None:
                starting_points.append(d) 

    return paths[sr, sc][2], f"({sr}, {sc})", min(starting_points)

if __name__ == '__main__':
    a1, start, a2 = answer1('input.txt')
    print(f"Answer 1: {a1} (start={start}).")
    print(f"Answer 2: {a2}.")