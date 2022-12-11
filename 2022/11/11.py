from typing import List, Dict
from dataclasses import dataclass

input = open("11/11.txt").readlines()

example = [
    "Monkey 0:",
    "Starting items: 79, 98",
    "Operation: new = old * 19",
    "Test: divisible by 23",
        "If true: throw to monkey 2",
        "If false: throw to monkey 3",
    "",
    "Monkey 1:",
    "Starting items: 54, 65, 75, 74",
    "Operation: new = old + 6",
    "Test: divisible by 19",
        "If true: throw to monkey 2",
        "If false: throw to monkey 0",
    "",
    "Monkey 2:",
    "Starting items: 79, 60, 97",
    "Operation: new = old * old",
    "Test: divisible by 13",
        "If true: throw to monkey 1",
        "If false: throw to monkey 3",
    "",
    "Monkey 3:",
    "Starting items: 74",
    "Operation: new = old + 3",
    "Test: divisible by 17",
        "If true: throw to monkey 0",
        "If false: throw to monkey 1"
]

@dataclass
class Monkey():
    items: List[int]
    operation: str
    testDiv: int
    monkeyIfTrue: int
    monkeyIfFalse: int

def analyseInput(input: List[str]) -> Dict[int, Monkey]:
    monkeys : Dict[int, Monkey] = {}
    for i in range(0, len(input), 7):
        nb = int(input[i].split()[1][:-1])
        items = [int(x) for x in input[i+1].split(':')[1].split(',')]
        operation = input[i+2].split('=')[1].strip()
        testDiv = int(input[i+3].split()[-1])
        ifTrue = int(input[i+4].split()[-1])
        ifFalse = int(input[i+5].split()[-1])
        monkeys[nb] = Monkey(items, operation, testDiv, ifTrue, ifFalse)
    return monkeys

def iterMonkey(nbMonkey: int, monkeys: Dict[int, Monkey], reduceWorryLevel: bool = True):
    m = monkeys[nbMonkey]
    while len(m.items):
        '''inspect'''
        m.items[0] = eval(m.operation.replace('old', 'm.items[0]'))
        '''divide'''
        if reduceWorryLevel:
            m.items[0] = int(m.items[0]/3)
        '''test'''
        if not m.items[0] % m.testDiv:
            '''give it to another'''
            monkeys[m.monkeyIfTrue].items.append(m.items.pop(0))
        else:
            monkeys[m.monkeyIfFalse].items.append(m.items.pop(0))

def runPart(monkeys: Dict[int, Monkey], rounds: int, reduceWorryLevel: bool):
    countedItems = [0]*len(monkeys)
    for i in range(rounds):
        for m in monkeys:
            countedItems[m] += len(monkeys[m].items)
            iterMonkey(m, monkeys, reduceWorryLevel)
    countedItems.sort()
    return countedItems[-1] * countedItems[-2]

def puzzle(input: List[str]):
    for i in range(len(input)):
        input[i] = input[i].strip()
    
    monkeys = analyseInput(input)
    part1 = runPart(monkeys, 20, True)
    monkeys = analyseInput(input)
    part2 = 0
    
    return (part1, part2)

try:
    assert(puzzle(example) == (10605, 0))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()