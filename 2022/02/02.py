input = open("02/02.txt").readlines()

example = [
"A Y",
"B X",
"C Z",
    ]

def puzzle(input):
    eq = {"X":"A", "Y":"B", "Z":"C"}
    winAgainst = {"A": "C", "B":"A", "C":"B"}
    shapeScore = {"A":1, "B":2, "C":3}

    part1 = 0
    for l in input:
        other, me = l.strip().split(' ')
        me = eq[me]
        part1 += shapeScore[me]
        if winAgainst[me] == other:
            part1 += 6
        elif me == other:
            part1 += 3

    part2=0
    for l in input:
        other, end = l.strip().split(' ')
        if end == "X":
            part2 += shapeScore[winAgainst[other]]
        if end == "Y":
            part2 += (3 + shapeScore[other])
        if end == "Z":
            part2 += (6 + sum([shapeScore[x] for x in shapeScore if winAgainst[x] == other]))
        
    return (part1, part2)


try:
    assert(puzzle(example) == (15, 12))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()