import utils

data = utils.getIntsFromFile("day1.input")

# data = [199,200,208,210,200,207,240,269,260,263]

def part1():
	inc = 0
	for i in range(1, len(data)):
		if data[i] > data[i-1]:
			inc += 1
	return inc

def part2():
	inc = 0
	for i in range(3, len(data)):
		if data[i] + data[i-1] + data[i-2] > data[i-1] + data[i-2] + data[i-3]:
			inc += 1
	return inc

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
