from helpers import loadMap, _width, _height, _left, _right, _top, _bottom

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

trees, width, height = loadMap()
print(f"Visible trees: {sum([1  for y in range(height) for x in range(width) if isVisibleFromOutside(x, y, trees) ])}.")
print(f"Highest scenic score: {max([scenicScore(x, y, trees) for x in range(width) for y in range(height)])}.")