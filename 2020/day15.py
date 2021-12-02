import utils
numbers = utils.getIntsFromFile("day15.input")

# numbers = [0,3,6]
# numbers = [3,1,2]

def part1():
	nb = [x for x in numbers]
	while len(nb) < 2020:
		if nb[-1] in nb[:-1]:
			nb.append(nb[-2::-1].index(nb[-1])+1)
		else:
			nb.append(0)
	return nb[-1]

def part2():
	turn = 1
	nb = {}
	last = 0
	for x in numbers:
		if x in nb:
			nb[x] = [turn, nb[x][0]]
		else:
			nb[x] = [turn, None]
		turn += 1
		last = x

	while turn <= 30000000:
		new = 0
		if last in nb:
			if nb[last][1]:
				new = nb[last][0] - nb[last][1]
		if new in nb:
			nb[new] = [turn, nb[new][0]]
		else:
			nb[new] = [turn, None]
		turn += 1
		last = new
	return last

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')