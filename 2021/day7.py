from statistics import median
import utils, sys
data = utils.getLinesFromFile("day7.input")

# data = ["16,1,2,0,4,2,7,1,2,14"]

def getCostPart2(a,b):
	dist = abs(a-b)
	return round((dist * (dist + 1)) / 2)

def part1():
	pos = [int(x) for x in data[0].split(',')]
	target = round(median(pos))
	ret = 0
	for p in pos:
		ret += abs(p-target)
	return ret

def part2():
	pos = [int(x) for x in data[0].split(',')]
	leastCost = sys.maxsize
	for target in range(min(pos), max(pos)):
		cost = 0
		for p in pos:
			cost += getCostPart2(target, p)
		# print(target, cost)
		leastCost = min(leastCost, cost)
	return leastCost

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
# utils.evalTime(10,part1)
# utils.evalTime(10,part2)