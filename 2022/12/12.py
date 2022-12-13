from typing import List, Dict, Tuple, Set

input = open("12/12.txt").readlines()

example = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi"
]


def getNeighbors(coords: Tuple[int, int]):
    available = []
    for y, x in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        available.append(tuple(sum(a) for a in list(zip(coords, (y,x)))))
    return available
        

def canGoThere(current: Tuple[int, int], target: Tuple[int, int], map: List[List[str]]) -> bool:
    # out of boundaries
    if target[0] < 0 or target[1] < 0 or target[0] >= len(map) or target[1] >= len(map[0]):
        return False
    
    # Start and End
    if map[current[0]][current[1]] == 'S':
        if map[target[0]][target[1]] == 'a':
            return True
        return False
    if map[target[0]][target[1]] == 'E':
        if map[current[0]][current[1]] == 'z':
            return True
        return False

    
    if ord(map[current[0]][current[1]]) <= ord(map[target[0]][target[1]]) <= ord(map[current[0]][current[1]]) + 1:
        return True
    if ord(map[current[0]][current[1]]) > ord(map[target[0]][target[1]]):
        return True
    return False

def mapFind(letter: str, map: List[List[str]]) -> Tuple[int, int]:
    res = []
    for y, i in enumerate(map):
        for x, j in enumerate(i):
            if j == letter:
                res.append((y, x))
    return res

def getH(current: Tuple[int, int], target: Tuple[int, int]) -> int:
    return abs(current[0] - target[0]) + abs(current[1] - target[1])

def reconstruct_path(cameFrom, current, map):
    total_path = [current,]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path

def getPathLen(startCoords: Tuple[int, int], endCoords: Tuple[int, int], map: List[str]) -> List[Tuple[int, int]]:
    openNodes: Set[Tuple[int, int]] = set([startCoords,])
    cameFrom: Dict[Tuple[int, int], Tuple[int, int]] = {}
    gScore: Dict[Tuple[int, int], int] = {startCoords: 0}
    fScore: Dict[Tuple[int, int], int] = {startCoords: getH(startCoords, endCoords) + gScore[startCoords]}
    current = startCoords
    while len(openNodes):
        current = sorted(openNodes, key=lambda n: fScore[n])[0]
        if current == endCoords:
            break
        openNodes.remove(current)
        for n in getNeighbors(current):
            if not canGoThere(current, n, map):
                continue
            n_gScore = gScore[current] + 1
            if n_gScore < gScore.get(n, 100_000):
                cameFrom[n] = current
                gScore[n] = n_gScore
                fScore[n] = getH(n, endCoords) + gScore[n]
                openNodes.add(n)
    return gScore[current]


def runPart1(map: List[str]) -> int:
    startCoords = mapFind('S', map)[0]
    endCoords = mapFind('E', map)[0]
    return getPathLen(startCoords, endCoords, map)

# my input's b height are all on the second column, and first column is full of a 
def runPart2(map: List[str]) -> int:
    endCoords = mapFind('E', map)[0]
    trailsLength = []
    for y in range(len(map)):
        trailsLength.append(getPathLen((y,0), endCoords, map))
    return min(trailsLength)

def puzzle(input: List[str]):
    for i in range(len(input)):
        input[i] = input[i].strip()
    
    part1 = runPart1(input)
    part2 = runPart2(input)
    
    return (part1, part2)

try:
    assert(puzzle(example) == (31, 29))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()