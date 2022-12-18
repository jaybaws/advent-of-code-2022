import sys

__input_file_name = 'input.txt'


def loadInput() -> dict:
    result = dict()
    with open(__input_file_name, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            x, y, z = map(int, line.split(","))
            result[line] = (x, y, z)
    return result
            

def answer1() -> int:
    coords = loadInput()
    max_sides = len(coords) * 6
    covered_sides = 0

    for s, (x,y,z) in coords.items():
        for dx, dy, dz in [(0,0,1), (0,1,0), (1, 0, 0), (0,0,-1), (0,-1,0), (-1,0,0)]:
            if f"{x+dx},{y+dy},{z+dz}" in coords:
                covered_sides += 1

    return max_sides - covered_sides


def floodfill(x:int, y:int, z:int, minimum:int, maximum:int, coords:set, filled:set, sides:list):
    if (x < minimum) or (y < minimum) or (z < minimum) or (x > maximum) or (y > maximum) or (z > maximum) or (x,y,z) in filled:
        return
    elif (x,y,z) in coords:
        sides.append((x,y,z))
    else:
        filled.add((x,y,z))
        for dx, dy, dz in [(0,0,1), (0,1,0), (1, 0, 0), (0,0,-1), (0,-1,0), (-1,0,0)]:
            floodfill(x+dx, y+dy, z+dz, minimum, maximum, coords, filled, sides)

def answer2() -> int:
    sys.setrecursionlimit(20000)  # :S

    coords = loadInput()
    maximum = max([max(x,y,z) for x,y,z in coords.values()]) + 1
    minimum = min([min(x,y,z) for x,y,z in coords.values()]) - 1

    filled = set([])
    sides = list([])
    coords = set([(x,y,z) for _, (x,y,z) in loadInput().items()])

    floodfill(minimum, minimum, minimum, minimum, maximum, coords, filled, sides)
    return len(sides)


def main() -> None:
    print(f"""
        Answer 1: {answer1()}.
        Answer 2: {answer2()}.
    """)

if __name__ == '__main__':
    main()