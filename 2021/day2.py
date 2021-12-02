import utils
data = utils.getLinesFromFile("day2.input")

# data = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']

def part1():
	dist, depth = 0, 0
	for d in data:
		dir, nb = d.split()
		if dir == "forward":
			dist += int(nb)
		if dir == "down":
			depth += int(nb)
		if dir == "up":
			depth -= nb
	ret = dist * depth
	return ret

def part2():
	dist, depth, aim = 0, 0, 0
	for d in data:
		dir, nb = d.split()
		if dir == "forward":
			dist += int(nb)
			depth += int(nb)*aim
		if dir == "down":
			aim += int(nb)
		if dir == "up":
			aim -= int(nb)
	ret = dist * depth
	return ret

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
