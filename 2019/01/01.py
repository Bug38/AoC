input = open("01/01.txt").readlines()

example1 = ["12"]
example2 = ["14"]
example3 = ["1969"]
example4 = ["100756"]

def puzzle(input):

    part1 = 0
    part2 = 0
    for l in input:
        fuel = int(int(l)/3)-2
        part1 += fuel
        part2 += fuel
        while fuel >= 9: # so fuel needed is >= 1
            fuel = int(int(fuel)/3)-2
            part2 += fuel

    return (part1, part2)


try:
    assert(puzzle(example1) == (2, 2))
    assert(puzzle(example2) == (2, 2))
    assert(puzzle(example3) == (654, 966))
    assert(puzzle(example4) == (33583, 50346))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example1)}")
    print(f"Error in examples, got {puzzle(example2)}")
    print(f"Error in examples, got {puzzle(example3)}")
    print(f"Error in examples, got {puzzle(example4)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()