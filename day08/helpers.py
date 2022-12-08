def loadMap() -> list[str]:
    input = open('input.txt', 'r')
    lines = [l.strip() for l in input.readlines()]
    input.close()
    return lines, _width(lines), _height(lines)

def _width(trees: list[str]) -> int:
    return max([len(l) for l in trees])

def _height(trees: list[str]) -> int:
    return len(trees)

def _left(x: int, y:int, map:list[str]) -> list[int]:
    return [int(h) for h in map[y][:x][::-1]]

def _right(x: int, y:int, map:list[str]) -> list[int]:
    return [int(h) for h in map[y][x+1:]]

def _top(x: int, y:int, map:list[str]) -> list[int]:
    return [int(map[y2][x]) for y2 in range(y-1, -1, -1)]

def _bottom(x: int, y:int, map:list[str]) -> list[int]:
    return [int(map[y2][x]) for y2 in range(y+1, _height(map))]