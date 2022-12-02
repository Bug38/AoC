input = "265275-781584"

example1 = "111111"
example2 = "223450"
example3 = "123789"


def is6digitsLong(password):
    return len(password) == 6

def increasingNumbers(password):
    for i in range(len(password)-1):
        if password[i] > password[i+1]:
            return False
    return True

def twoAdjascentAreSame(password:str):
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            password.count(password[i])
            return True
    return False

def isOk(password, r):
    return is6digitsLong(password) and increasingNumbers(password) and twoAdjascentAreSame(password)

def puzzle(input):

    r = input.split('-')
    part1 = 0
    part2 = 0
    for i in range(int(r[0]), int(r[1])+1):
        if isOk(str(i), r):
                part1 += 1
                if 2 in [str(i).count(x) for x in str(i)]:
                    part2 += 1
    return (part1, part2)

try:
    assert(isOk(example1, ['000000','999999']) == True)
    assert(isOk(example2, ['000000','999999']) == False)
    assert(isOk(example3, ['000000','999999']) == False)
except AssertionError as e:
    print(f"Error in examples, got {isOk(example1, ['000000','999999'])}")
    print(f"Error in examples, got {isOk(example2, ['000000','999999'])}")
    print(f"Error in examples, got {isOk(example3, ['000000','999999'])}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()