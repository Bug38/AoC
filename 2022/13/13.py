from typing import List, Dict, Tuple, Set
from ast import literal_eval

input = open("13/13.txt").readlines()

example = [
    "[1,1,3,1,1]",
    "[1,1,5,1,1]",
    "",
    "[[1],[2,3,4]]",
    "[[1],4]",
    "",
    "[9]",
    "[[8,7,6]]",
    "",
    "[[4,4],4,4]",
    "[[4,4],4,4,4]",
    "",
    "[7,7,7,7]",
    "[7,7,7]",
    "",
    "[]",
    "[3]",
    "",
    "[[[]]]",
    "[[]]",
    "",
    "[1,[2,[3,[4,[5,6,7]]]],8,9]",
    "[1,[2,[3,[4,[5,6,0]]]],8,9]"
]

def getListDepth(l: list, startDepth: int = 0):
    if len(l) == 0:
        return 1
    depth = [startDepth + 1] * len(l)
    for i in range(len(l)):
        if type(l[i]) == list:
            depth[i] += getListDepth(l[i])
        else:
            depth[i] += 0
    return max(depth)

def setListDepth(l: list, targetDepth: int, startDepth: int = 1):
    if targetDepth == startDepth:
        return
    for i in range(len(l)):
        if type(l[i]) == list:
            setListDepth(l[i], targetDepth, startDepth + 1)
        else:
            a = l[i]
            for _ in range(targetDepth - startDepth):
                a = [a]
            l[i] = a
    return l

def runPart1(input):
    part1 = 0
    currentPair = 1
    for i in range(0, len(input), 3):
        list1 = literal_eval(input[i])
        list2 = literal_eval(input[i+1])
        neededDepth = max(getListDepth(list1), getListDepth(list2))
        setListDepth(list1, neededDepth)
        setListDepth(list2, neededDepth)
        if list1 < list2:
            part1 += currentPair
        currentPair += 1
    return part1

def runPart2(input):
    lists = {i: literal_eval(i) for i in input + ["[[2]]","[[6]]"] if i != ''}
    maxDepth = max([getListDepth(lists[l]) for l in lists])
    sortedLists = sorted([l for l in lists], key=lambda l: setListDepth(lists[l], maxDepth))
    return (sortedLists.index("[[2]]") + 1) * (sortedLists.index("[[6]]") + 1)
    

def puzzle(input: List[str]):
    for i in range(len(input)):
        input[i] = input[i].strip()

    part1 = runPart1(input)
    part2 = runPart2(input)
    
    return (part1, part2)

try:
    assert(puzzle(example) == (13, 140))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()