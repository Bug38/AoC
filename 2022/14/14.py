from typing import List, Dict, Tuple, Set
from ast import literal_eval

input = open("14/14.txt").readlines()

example = [
    "498,4 -> 498,6 -> 496,6",
    "503,4 -> 502,4 -> 502,9 -> 494,9"
]

''' returns sand if not fixed, else None'''
def fallSand(sand: Tuple[int, int], map: Set[Tuple[int, int]]):
    if not (sand[0] + 1, sand[1]) in map:
        return (sand[0] + 1, sand[1])
    if not (sand[0] + 1, sand[1] - 1) in map:
        return (sand[0] + 1, sand[1] - 1)
    if not (sand[0] + 1, sand[1] + 1) in map:
        return (sand[0] + 1, sand[1] + 1)
    map.add(sand)
    return None

def getPath(nodes: List[str]) -> Set[Tuple[int, int]]:
    path = set()
    for n in range(len(nodes)-1):
        x1, y1 = (int(a) for a in nodes[n].split(','))
        x2, y2 = (int(a) for a  in nodes[n+1].split(','))
        dy = y2 - y1
        dx = x2 - x1
        if dy :
            sign = int(abs(dy)/dy)
            path.update([(y, x1) for y in range(y1, y2 + sign, sign)])
        elif dx :
            sign = int(abs(dx)/dx)
            path.update([(y1, x) for x in range(x1, x2 + sign, sign)])
        else:
            path.update([(y1, x1)])
    return path

def traceMap(input: List[str], part2: bool = False) -> Set[Tuple[int, int]]:
    map = set()
    for i in input:
        map.update(getPath(i.split(' -> ')))
    if part2:
        lowestY = getLowestLevel(map)
        lowestX = sorted(list(map), key=lambda n: n[1])[0][1]
        largestX = sorted(list(map), key=lambda n: n[1])[-1][1]
        map.update(getPath([f'{lowestX-1000}, {lowestY+2}', f'{largestX+1000}, {lowestY+2}']))
    return map

def getLowestLevel(map: set[Tuple[int, int]]) -> int:
    lowest = 0
    for p in map:
        lowest = max(p[0], lowest)
    return lowest

def run(input: List[str], part2: bool = False):
    map = traceMap(input, part2)
    lowest = getLowestLevel(map)
    mapSize = 0
    falledSands = 0
    while mapSize != len(map):
        mapSize = len(map)
        sand = (0, 500)
        while sand:
            if sand[0] > lowest+3:
                break
            sand = fallSand(sand, map)
        falledSands += 1
    return falledSands -1
            
def puzzle(input: List[str]):
    for i in range(len(input)):
        input[i] = input[i].strip()

    part1 = run(input)
    part2 = run(input, True)
    
    return (part1, part2)

try:
    assert(puzzle(example) == (24, 93))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()