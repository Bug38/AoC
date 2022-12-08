from typing import List, Tuple

input = open("08/08.txt").readlines()

example = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390"
    ]

def isVisible(treePos: Tuple[int, int], input: List[str]):
    ''' Top '''
    visible = 4
    for y in range(0, treePos[0]):
        if input[y][treePos[1]] >= input[treePos[0]][treePos[1]]:
            visible -= 1
            break
    ''' Bottom '''
    for y in range(treePos[0]+1, len(input)):
        if input[y][treePos[1]] >= input[treePos[0]][treePos[1]]:
            visible -= 1
            break
    ''' Left '''
    for x in range(0, treePos[1]):
        if input[treePos[0]][x] >= input[treePos[0]][treePos[1]]:
            visible -= 1
            break
    ''' Right '''
    for x in range(treePos[1]+1, len(input[0])):
        if input[treePos[0]][x] >= input[treePos[0]][treePos[1]]:
            visible -= 1
            break
    return visible > 0

def scenicScore(treePos: Tuple[int, int], input: List[str]):
    score = [0,0,0,0]
    ''' Top '''
    for y in range(treePos[0]-1, -1, -1):
        score[0] += 1
        if input[y][treePos[1]] >= input[treePos[0]][treePos[1]]:
            break
    ''' Left '''
    for x in range(treePos[1]-1, -1, -1):
        score[2] += 1
        if input[treePos[0]][x] >= input[treePos[0]][treePos[1]]:
            break
    ''' Bottom '''
    for y in range(treePos[0]+1, len(input)):
        score[1] += 1
        if input[y][treePos[1]] >= input[treePos[0]][treePos[1]]:
            break
    ''' Right '''
    for x in range(treePos[1]+1, len(input[0])):
        score[3] += 1
        if input[treePos[0]][x] >= input[treePos[0]][treePos[1]]:
            break
    return score[0] * score[1] * score[2] * score[3]

    
def runPart1(input: List[str]):
    part1 = 2 * (len(input) + len(input[0]) - 2)
    for y in range(1, len(input) - 1):
        for x in range(1, len(input[0]) - 1):
            if isVisible((y,x), input):
                part1 += 1
    return part1

def runPart2(input: List[str]):
    scores = []
    for y in range(0, len(input)):
        for x in range(0, len(input[0])):
            scores.append(scenicScore((y,x), input))
    return max(scores)

def puzzle(input: List[str]):
    for i in range(len(input)):
        input[i] = input[i].strip()

    part1 = runPart1(input)
    part2 = runPart2(input)
    
    return (part1, part2)


try:
    assert(puzzle(example) == (21, 8))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()