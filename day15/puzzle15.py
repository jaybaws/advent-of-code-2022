from typing import Tuple, Set
from parse import parse

__input_file_name = 'input.txt'
__line = 2_000_000
__max = 4_000_000

# __input_file_name = 'input_sample.txt'
# __line = 10
# __max = 20

def loadInput() -> Set[Tuple[int, int, int, int]]:
    with  open(__input_file_name, 'r') as f:
        def myParser(s: str) -> Tuple[int, int, int, int]:
            sx, sy, bx, by = parse("Sensor at x={}, y={}: closest beacon is at x={}, y={}", s)
            return (int(sx), int(sy), int(bx), int(by))

        return list(map(myParser, f.read().splitlines()))


def mannhattan_distance(p1:int, p2:int, q1:int, q2:int) -> int:
    return abs(p1-q1) + abs(p2-q2)


def tuning_frequency(x:int, y:int) -> int:
    return 4_000_000 * x + y


def answer1(input: Set[Tuple[int, int, int, int]]) -> int:
    invalid_points = set([])
    beacons_on_line = set([x for (_, _, x, y) in input if y == __line])

    for (sx, sy, bx, by) in input:
        d = mannhattan_distance(sx, sy, bx, by)
        if (sy - d) <= __line <= (sy + d):
            offset = abs(__line - sy)
            r = range(sx - d + offset, sx + d - offset + 1)
            invalid_points.update(r)

    return len(invalid_points) - len(beacons_on_line)


def coverage(x:int, input: Set[Tuple[int, int, int, int]]) -> list[range]:
    result = list([])
    for (sx, sy, bx, by) in input:
        d = mannhattan_distance(sx, sy, bx, by)
        offset = abs(x - sx)
        if (sx - d) <= x <= (sx + d):
            result.append(range(sy - d + offset, sy + d - offset))
    return result


def answer2(input: Set[Tuple[int, int, int, int]]) -> int:
    for x in range(__max + 1):
        # Sort the ranges, so we can test for sequential continuity of the ranges
        ranges = sorted(coverage(x, input), key=lambda x: x.start)

        until = ranges[0].stop
        for i in range(1, len(ranges) - 1):
            if ranges[i].start <= until + 1:
                until = max(until, ranges[i].stop)
            else:
                return tuning_frequency(x, until + 1)
    
    return None  # Just in case ;-)


if __name__ == '__main__':
    input = loadInput()
    a1, a2 = answer1(input), answer2(input)

    print(f"""
        Answer 1: {a1}.
        Answer 2: {a2}.
    """)


# *** Thoughts directly after completion:
# - Struggled with second part too long.
#   - Took a while to figure out how do deal with the size/duration challenge
#     -> Looping the entire 4mio x 4mio matrix would take too long.
#     -> Keeping track of visited points would take too much memory
#   - Once I understood I could verify 1-dimenstional on one axis, I
#     struggled too long to play with ranges.
#     -> Tried to find a way to test if a range is continuous, but couldn't
#        figure that out.
#        -> Settled for comparing the ranges and spotting 'gaps'. 
# - First part was okay though

# *** Thoughts after seeing other people's solutions:
# - Could have calculated the manhattan distance right at parse time.
# - Could have not used the range object, but just a (start,end) tuple.

# *** Learnings:
# - parse library. Nice!