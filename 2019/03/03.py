input = open("03/03.txt").readlines()

example1 = [
    "R8,U5,L5,D3",
    "U7,R6,D4,L4"
]
example2 = [
    "R75,D30,R83,U83,L12,D49,R71,U7,L72",
    "U62,R66,U55,R34,D71,R55,D58,R83"]
example3 = [
    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
    "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]

d = {
    "U":( 0,-1),
    "D":( 0, 1),
    "R":( 1, 0),
    "L":(-1, 0),
}

def getPath(dir, dist, origin):
    path = []
    for _ in range(dist):
        origin = tuple(sum(x) for x in zip(origin,d[dir]))
        path.append(origin)
    return path

def runPart1(input):
    wires = [set(), set()]
    for i in [0,1]:
        org = (0,0)
        for p in input[i].split(','):
            path = getPath(p[0], int(p[1:]), org)
            org = path[-1]
            wires[i].update(path)
    return min([sum((abs(x), abs(y))) for (x,y) in wires[0] if (x,y) in wires[1]])

def runPart2(input):
    wires = [set(), set()]
    timeToCoord = {(0,0) : [0, 0]}
    for w in [0,1]:
        org = (0,0)
        for i in input[w].split(','):
            path = getPath(i[0], int(i[1:]), org)
            wires[w].update(path)
            for nb, p in enumerate(path):
                if not p in timeToCoord:
                    timeToCoord[p] = [1000000,10000000]
                timeToCoord[p][w] = min(timeToCoord[p][w], nb + timeToCoord[org][w] + 1)
            org = path[-1]
    nodes = [x for x in wires[0] if x in wires[1]]
    return min([sum([abs(a) for a in timeToCoord[x]]) for x in nodes])

def puzzle(input):

    part1 = runPart1(input)
    part2 = runPart2(input)

    return (part1, part2)


try:
    assert(puzzle(example1) == (6, 30))
    assert(puzzle(example2) == (159, 610))
    assert(puzzle(example3) == (135, 410))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example1)}")
    print(f"Error in examples, got {puzzle(example2)}")
    print(f"Error in examples, got {puzzle(example3)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()