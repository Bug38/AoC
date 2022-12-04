input = open("04/04.txt").readlines()

example = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
    ]


def puzzle(input):

    part1 = 0
    part2 = 0
    
    for i in input:
        lims = i.strip().split(',')
        s = []
        for i, l in enumerate(lims):
            l1, l2 = list([int(a) for a in l.split('-')])
            s.append(set(range(int(l1), int(l2)+1)))
        if s[0].issubset(s[1]) or s[1].issubset(s[0]):
            part1 += 1
        if s[0].intersection(s[1]) != set():
            part2 += 1
        
    return (part1, part2)


try:
    assert(puzzle(example) == (2, 4))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()