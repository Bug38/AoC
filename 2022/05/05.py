import re

input = open("05/05.txt").readlines()

example = [
"    [D]    ",
"[N] [C]    ",
"[Z] [M] [P]",
 "1   2   3 ",
"",
"move 1 from 2 to 1",
"move 3 from 1 to 3",
"move 2 from 2 to 1",
"move 1 from 1 to 2",
    ]

def parseInput(input):
    parsingInstruction = False
    stacks = {}
    for line, i in enumerate(input):
        if i.strip() == '':
            return stacks, input[line+1:]
        if parsingInstruction:
            continue
        for _i in range(1, len(i), 4):
            col = int(_i/4) + 1
            if not col in stacks:
                stacks[col] = []
            if i[_i] == ' ':
                continue
            stacks[col].insert(0,i[_i])

def runPart1(stacks, instructions):
    for i, inst in enumerate(instructions):
        _nb, _from, _to = [int(x) for x in re.findall(r'\d+', inst)]
        for _ in range(_nb):
            stacks[_to].append(stacks[_from].pop())
    return ''.join(stacks[x][-1] for x in stacks)
    
def runPart2(stacks, instructions):
    for i, inst in enumerate(instructions):
        _nb, _from, _to = [int(x) for x in re.findall(r'\d+', inst)]
        stacks[_to] += stacks[_from][-_nb:]
        stacks[_from] = stacks[_from][:-_nb]
    return ''.join(stacks[x][-1] for x in stacks)

def puzzle(input):
    
    part1 = runPart1(*parseInput(input))
    part2 = runPart2(*parseInput(input))
        
    return (part1, part2)


try:
    assert(puzzle(example) == ('CMZ', 'MCD'))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()