import utils
instructions = utils.getLinesFromFile("day12.input")

# instructions = ['F10','N3','F7','R90','F11']

def part1():
	direction = 'E'
	cardinals = ['N', 'E', 'S', 'W']
	posEW, posNS = 0,0

	def applyInstruction(instruction):
		nonlocal posNS, posEW, direction
		i, nb = instruction[0], int(instruction[1:])
		if i == 'F':
			i = direction
		if i == 'N':
			posNS += nb
		if i == 'S':
			posNS -= nb
		if i == 'E':
			posEW += nb
		if i == 'W':
			posEW -= nb
		if i == 'R':
			direction = cardinals[(cardinals.index(direction) + int(nb / 90)) % 4]
		if i == 'L':
			direction = cardinals[(cardinals.index(direction) - int(nb / 90)) % 4]

	for i in instructions:
		applyInstruction(i)
	return abs(posEW) + abs(posNS)

def part2():
	posEW, posNS = 0,0
	waypointEW, waypointNS = 10, 1

	def applyInstruction(instruction):
		nonlocal posEW, posNS, waypointEW, waypointNS
		i, nb = instruction[0], int(instruction[1:])
		if i == 'F':
			posEW, posNS = posEW + nb * waypointEW, posNS + nb * waypointNS
		if i == 'N':
			waypointNS += nb
		if i == 'S':
			waypointNS -= nb
		if i == 'E':
			waypointEW += nb
		if i == 'W':
			waypointEW -= nb
		if i == 'R':
			for i in range(int(nb/90)):
				waypointEW, waypointNS = waypointNS, -waypointEW
		if i == 'L':
			for i in range(int(nb/90)):
				waypointEW, waypointNS = -waypointNS, waypointEW
		return

	for i in instructions:
		applyInstruction(i)
	return abs(posEW) + abs(posNS)


print(f'Part1: {part1()}')
print(f'Part2: {part2()}')