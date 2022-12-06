input = open("06/06.txt").readlines()

example = [
"mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    ]

def getIndiceForPartX(input, uniquechar):
    for i, _ in enumerate(input):
        if max([input[i:i+uniquechar].count(x) for x in input[i:i+uniquechar]]) == 1:
            return i+uniquechar

def puzzle(input):
    
    part1 = getIndiceForPartX(input[0], 4)
    part2 = getIndiceForPartX(input[0], 14)
        
    return (part1, part2)


try:
    assert(puzzle(example) == (7, 19))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()