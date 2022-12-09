from typing import List, Tuple
from dataclasses import dataclass

input = open("09/09.txt").readlines()

example = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2"
    ]

example2 = [
    "R 5",
    "U 8",
    "L 8",
    "D 3",
    "R 17",
    "D 10",
    "L 25",
    "U 20"
]

moveX = {'U':0, 'D':0, 'L':-1, 'R':1}
moveY = {'U':-1, 'D':1, 'L':0, 'R':0}

@dataclass
class Point():
    x: int
    y: int
    def moveIfTooFar(self, p):
        diffx, diffy = p.x - self.x, p.y - self.y
        if abs(diffx) > 1:
            self.move('R' if diffx > 1 else 'L')
            if abs(diffy) > 0:
                self.move('D' if diffy > 0 else 'U')
        elif abs(diffy) > 1:
            self.move('D' if diffy > 1 else 'U')
            if abs(diffx) > 0:
                self.move('R' if diffx > 0 else 'L')
        return self
    def move(self, dir: str):
        self.x += moveX[dir]
        self.y += moveY[dir]
        return self

def runPart1(input: List[str]):
    H = Point(0,0)
    T = Point(0,0)
    TailPosSet = set()
    i = 0
    while i != len(input):
        d, n = input[i].split()[0], int(input[i].split()[1])
        while n > 0:
            H.move(d)
            T.moveIfTooFar(H)
            TailPosSet.add((T.x, T.y))
            n -= 1
        i += 1
    return len(list(TailPosSet))

def runPart2(input: List[str]):
    R = []
    for _ in range(10):
        R.append(Point(0,0))
    TailPosSet = set()
    i = 0
    while i != len(input):
        d, n = input[i].split()[0], int(input[i].split()[1])
        while n > 0:
            R[0].move(d)
            for ir in range(1, len(R)):
                R[ir].moveIfTooFar(R[ir-1])
                TailPosSet.add((R[-1].x, R[-1].y))
            n -= 1
        i += 1
    return len(list(TailPosSet))


def puzzle(input: List[str]):
    for i in range(len(input)):
        input[i] = input[i].strip()

    part1 = runPart1(input)
    part2 = runPart2(input)
    
    return (part1, part2)


try:
    assert(puzzle(example) == (13, 1))
    assert(puzzle(example2) == (88, 36))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    print(f"Error in examples, got {puzzle(example2)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()