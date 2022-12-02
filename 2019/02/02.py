input = open("02/02.txt").readlines()

example = ["1,9,10,3,2,3,11,0,99,30,40,50"]


def runCode(code: str):
    currentIndex = 0
    while code[currentIndex] != 99:
        if code[currentIndex] == 1:
            code[code[currentIndex+3]] = code[code[currentIndex+1]] + code[code[currentIndex+2]]
        if code[currentIndex] == 2:
            code[code[currentIndex+3]] = code[code[currentIndex+1]] * code[code[currentIndex+2]]
        currentIndex += 4
    return code


def puzzle(input):
    part1 = 0
    part2 = 0
    
    inputPart1 = [int(x) for x in input[0].split(',')]
    inputPart1[1] = 12
    inputPart1[2] = 2
    part1 = runCode(inputPart1)[0]

    for noun, verb in ((n,v) for n in range(100) for v in range(100)):
        inputPart2 = [int(x) for x in input[0].split(',')]
        inputPart2[1] = noun
        inputPart2[2] = verb
        if runCode(inputPart2)[0] == 19690720:
            part2 = 100*noun + verb
            break

    return (part1, part2)


try:
    example = [int(x) for x in example[0].split(',')]
    assert(runCode(example)[0] == 3500)
except AssertionError as e:
    print(f"Error in examples, got {runCode(example)[0]}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()