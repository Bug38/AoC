input = open("03/03.txt").readlines()

example = [
"vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

def getLetterValue(l):
    if l.islower():
        return ord(l) - ord('a') + 1
    else:
        return ord(l) - ord('A') + 27

def puzzle(input):

    part1 = 0
    part2 = 0

    for rucksack in input:
        rucksack = rucksack.strip()
        clen = int(len(rucksack)/2)
        c1, c2 = rucksack[:clen], rucksack[clen:]
        common = ''.join(set(c1).intersection(c2))
        part1 += getLetterValue(common)

    for i in range(0, len(input), 3):
        r1, r2, r3 = input[i].strip(), input[i+1].strip(), input[i+2].strip()
        common = ''.join(set(r1).intersection(r2).intersection(r3))
        part2 += getLetterValue(common)
        
    return (part1, part2)


try:
    assert(puzzle(example) == (157, 70))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()