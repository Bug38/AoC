input = open("01/01.txt").readlines()

example = ["1000",
"2000",
"3000",
"",
"4000",
"",
"5000",
"6000",
"",
"7000",
"8000",
"9000",
"",
"10000"]


def puzzle(input):
    part1 = 0
    current = 0
    elves = []

    for l in input:
        if l.strip() == "":
            part1 = max(current, part1)
            elves.append(current)
            current = 0
            continue
        current += int(l)
    elves.append(current)
    part1 = max(current, part1)

    part2 = sum(sorted(elves)[-3:])
    return (part1, part2)


try:
    assert(puzzle(example) == (24000, 45000))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()