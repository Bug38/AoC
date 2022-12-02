input = open("02/02.txt").readlines()

input2 = [
"A Y",
"B X",
"C Z",
    ]

shapeScore = {"X":1, "Y":2, "Z":3}

part1 = 0
for l in input:
    other, me = l.strip().split(' ')
    part1 += shapeScore[me]
    if me == "X":
        if other == "C":
            part1 += 6
        elif other == "A":
            part1 += 3
    if me == "Y":
        if other == "A":
            part1 += 6
        elif other == "B":
            part1 += 3
    if me == "Z":
        if other == "B":
            part1 += 6
        elif other == "C":
            part1 += 3

looseAgainst = {"A": "B", "B":"C", "C":"A"}
shapeScore = {"A":1, "B":2, "C":3}

part2=0
for l in input:
    other, end = l.strip().split(' ')
    if end == "X":
        part2 += sum([shapeScore[x] for x in looseAgainst if looseAgainst[x] == other])
    if end == "Y":
        part2 += (3 + shapeScore[other])
    if end == "Z":
        part2 += (6 + shapeScore[looseAgainst[other]])

print(f'{part1=}')
print(f'{part2=}')
print()