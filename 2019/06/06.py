input = open("06/06.txt").readlines()

example1 = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L"
]
example2 = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L",
    "K)YOU",
    "I)SAN",
]

def getMap(input):
    omap = {}
    for i in input:
        a,b = i.strip().split(')')
        omap[b] = a
    return omap

def getPath(omap, start):
    path = []
    curr = start
    while curr != 'COM':
        curr = omap[curr]
        path.append(curr)
    return path

def runPart1(omap):
    orbits = 0
    for o in omap:
        orbits += len(getPath(omap, o))
    return orbits

def runPart2(omap):
    startPath = getPath(omap, "YOU")
    endPath = getPath(omap, "SAN")
    for o in startPath:
        if o in endPath:
            return startPath.index(o) + endPath.index(o)

    
def puzzle(input):

    part1 = 0
    part2 = 0

    omap = getMap(input)
    part1 = runPart1(omap)
    if 'YOU' in omap and 'SAN' in omap:
        part2 = runPart2(omap)

    return (part1, part2)


try:
    assert(puzzle(example1) == (42, 0))
    assert(puzzle(example2) == (54, 4))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example1)}")
    print(f"Error in examples, got {puzzle(example2)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()