from copy import deepcopy
import utils
data = utils.getLinesFromFile("day11.input")

# data = ['5483143223','2745854711','5264556173','6141336146','6357385478','4167524645','2176841721','6882881134','4846848554','5283751526']

octopusses = [[int(x) for x in d] for d in data]
cptBlinkPart1 = 0

def increaseAll(src):
	return [[x+1 for x in d] for d in src]

def blinkOne(src):
	global cptBlinkPart1
	ret = deepcopy(src)
	for y in range(len(ret)):
		for x in range(len(ret[y])):
			if ret[y][x] > 9:
				for xx,yy in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
					if len(ret[y]) > xx+x >= 0 and len(ret) > yy + y >= 0:
						if ret[yy+y][xx+x] >= 0:
							ret[yy+y][xx+x] += 1
				ret[y][x] = -1
				cptBlinkPart1 += 1
				return True, ret
	return False, None

def resetBlinked(src):
	ret = deepcopy(src)
	for y in range(len(ret)):
		for x in range(len(ret[y])):
			if ret[y][x] == -1:
							ret[y][x] =0
	return ret

def iterOneStep(src):
	grid = increaseAll(src)
	blinked = True
	while blinked:
		blinked, r = blinkOne(grid)
		grid = r or grid
	return resetBlinked(grid)

def part1():
	grid = deepcopy(octopusses)
	for i in range(100):
		grid = iterOneStep(grid)
	return cptBlinkPart1

def part2():
	grid = deepcopy(octopusses)
	for i in range(1000):
		grid = iterOneStep(grid)
		if grid == [[0]*len(grid[0])]*len(grid):
			return i+1
	return cptBlinkPart1

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
