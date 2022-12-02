import utils
data = utils.getLinesFromFile("day9.input")

# data = ['2199943210','3987894921','9856789892','8767896789','9899965678']

heightmap = {}
for y, d in enumerate(data):
	for x, dd in enumerate(d):
		heightmap[(x,y)] = int(dd)

def getNeighboursC(c):
	x, y = c
	return [(xx,yy) for xx, yy in [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]]


def part1():
	ret = 0
	for c in heightmap:
		neightbours = [heightmap.get((xx,yy), 9) for xx, yy in getNeighboursC(c)]
		if min(neightbours) > heightmap[c]:
			ret += (heightmap[c] + 1)
	return ret

def defineBasin(b):
	ret = []
	outer = []
	for c in b:
		n = getNeighboursC(c)
		for i in n:
			if heightmap.get(i, 9) < 9 and not i in b and not i in outer:
				outer.append(i)
	if len(outer) == 0:
		return []
	return outer + defineBasin(b + outer)

def part2():
	deepests = []
	for c in heightmap:
		neightbours = [heightmap.get((xx,yy), 9) for xx, yy in getNeighboursC(c)]
		if min(neightbours) > heightmap[c]:
			deepests.append(c)
	basins = []
	for d in deepests:
		allreadyCount = False
		for b in basins:
			if d in b :
				allreadyCount = True
				break
		if allreadyCount: 
			continue
		basins.append([d] + defineBasin([d]))

	ret = 1
	for b in sorted(basins, key=len)[-3:]:
		ret *= len(b)
	return ret

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')