import utils
data = utils.getLinesFromFile("day6.input")

# data = ["3,4,3,1,2"]

lanternfishs = [int(x) for x in data[0].split(',')]

def getFishsAfter(days):
	fishs = lanternfishs.copy()
	for _ in range(days):
		newfishs = []
		for f in fishs:
			if f > 0:
				newfishs.append(f-1)
			else:
				newfishs.append(6)
				newfishs.append(8)
		fishs = newfishs.copy()
	return len(fishs)

def getFishsAfterBig(days):
	fishs = {}
	for f in lanternfishs:
		fishs[f] = fishs.get(f, 0) + 1
	for _ in range(days):
		# print([(f, fishs[f]) for f in fishs])
		newfishs = {}
		for f in fishs:
			if f > 0:
				newfishs[f-1] = newfishs.get(f-1, 0) + fishs[f]
			else:
				newfishs[6] = newfishs.get(6, 0) + fishs[f]
				newfishs[8] = fishs[f]
		fishs = newfishs.copy()
	
	ret = 0
	for f in fishs:
		ret += fishs[f]
	return ret


def part1():
	return getFishsAfterBig(80)

def part2():
	return getFishsAfterBig(256)

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
utils.evalTime(10,part1)
utils.evalTime(10,part2)