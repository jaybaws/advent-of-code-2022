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

def isVisibleFromOutside(x: int, y:int, trees:list[str]) -> bool:
    if x == 0 or y == 0 or x >= _width(trees)-1 or y >= _height(trees)-1:
        return True
    else:
        tree_height = int(trees[y][x])
        return (
            tree_height > max(_left(x,y,trees)) or
            tree_height > max(_right(x,y,trees)) or 
            tree_height > max(_top(x,y,trees)) or
            tree_height > max(_bottom(x,y,trees))
        )

def freeSightDistance(tree_height: int, neighbours:list[str]) -> int:
    visibility = 0
    for neighbour in neighbours:
        visibility += 1
        if neighbour >= tree_height:
            break
    return visibility

def scenicScore(x: int, y:int, trees:list[str]) -> int:
    h = int(trees[y][x])
    return (
        freeSightDistance(h, _left(x, y, trees)) * 
        freeSightDistance(h, _right(x, y, trees)) * 
        freeSightDistance(h, _top(x, y, trees)) * 
        freeSightDistance(h, _bottom(x, y, trees))
    )

def part1() -> int:
    trees, width, height = loadMap()
    visible_trees = 0
    for y in range(height):
        for x in range(width):
            if isVisibleFromOutside(x, y, trees):
                visible_trees += 1
    return visible_trees

def part2() -> int:
    trees, width, height = loadMap()
    sight_scores = [scenicScore(x, y, trees) for x in range(width) for y in range(height)]
    return max(sight_scores)

print(f"Visible trees: {part1()}.")
print(f"Highest scenic score: {part2()}.")