from typing import List
from dataclasses import dataclass

input = open("10/10.txt").readlines()

example = [
    "noop",
    "addx 3",
    "addx -5"
]

example2 = ["addx 15", "addx -11", "addx 6", "addx -3", "addx 5", "addx -1", "addx -8", "addx 13", "addx 4", "noop", "addx -1", "addx 5", "addx -1", "addx 5", "addx -1", "addx 5", "addx -1", "addx 5", "addx -1", "addx -35", "addx 1", "addx 24", "addx -19", "addx 1", "addx 16", "addx -11", "noop", "noop", "addx 21", "addx -15", "noop", "noop", "addx -3", "addx 9", "addx 1", "addx -3", "addx 8", "addx 1", "addx 5", "noop", "noop", "noop", "noop", "noop", "addx -36", "noop", "addx 1", "addx 7", "noop", "noop", "noop", "addx 2", "addx 6", "noop", "noop", "noop", "noop", "noop", "addx 1", "noop", "noop", "addx 7", "addx 1", "noop", "addx -13", "addx 13", "addx 7", "noop", "addx 1", "addx -33", "noop", "noop", "noop", "addx 2", "noop", "noop", "noop", "addx 8", "noop", "addx -1", "addx 2", "addx 1", "noop", "addx 17", "addx -9", "addx 1", "addx 1", "addx -3", "addx 11", "noop", "noop", "addx 1", "noop", "addx 1", "noop", "noop", "addx -13", "addx -19", "addx 1", "addx 3", "addx 26", "addx -30", "addx 12", "addx -1", "addx 3", "addx 1", "noop", "noop", "noop", "addx -9", "addx 18", "addx 1", "addx 2", "noop", "noop", "addx 9", "noop", "noop", "noop", "addx -1", "addx 2", "addx -37", "addx 1", "addx 3", "noop", "addx 15", "addx -21", "addx 22", "addx -6", "addx 1", "noop", "addx 2", "addx 1", "noop", "addx -10", "noop", "noop", "addx 20", "addx 1", "addx 2", "addx 2", "addx -6", "addx -11", "noop", "noop", "noop"]
example2_result = "##..##..##..##..##..##..##..##..##..##..###...###...###...###...###...###...###.####....####....####....####....####....#####.....#####.....#####.....#####.....######......######......######......###########.......#######.......#######....."

@dataclass
class registers:
    x: int
    tmp: int

def exec(reg: registers, instr: str): # returns the shift to do in the program (next instr) 
    if instr == "noop":
        return 1
    else:
        value = int(instr.split()[1])
        if reg.tmp != 0:
            reg.x += reg.tmp
            reg.tmp = 0
            return 1
        else:
            reg.tmp = value
            return 0
            
def runPart1(input):
    reg = registers(1, 0)
    i, cycle = 0, 0
    part1 = 0
    while i < len(input):
        cycle += 1
        if cycle == 20 or (cycle-20) % 40 == 0:
            part1 += reg.x * cycle
        shift = exec(reg, input[i])
        i += shift
    return part1

def runPart2(input):
    reg = registers(1, 0)
    i, cycle = 0, 0
    part2 = ""
    while i < len(input):
        if reg.x-1 <= cycle%40 <= reg.x+1:
            part2 += '#'
        else:
            part2 += '.'
        cycle += 1
        shift = exec(reg, input[i])
        i += shift
    return part2

def printCRT(crt: str):
    for i, c in enumerate(crt):
        if i%40 == 0:
            print()
        print(c, end='')
    print()


def puzzle(input: List[str]):
    for i in range(len(input)):
        input[i] = input[i].strip()

    part1 = runPart1(input)
    part2 = runPart2(input)
    
    return (part1, part2)


try:
    # assert(puzzle(example) == (0, 0))
    assert(puzzle(example2) == (13140, example2_result))
except AssertionError as e:
    # print(f"Error in examples, got {puzzle(example)}")
    print(f"Error in examples, got {puzzle(example2)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print('part2=')
printCRT(part2)
print()