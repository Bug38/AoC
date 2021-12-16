import utils
data = utils.getLinesFromFile("day5.input")

# data = ['0,9 -> 5,9','8,0 -> 0,8','9,4 -> 3,4','2,2 -> 2,1','7,0 -> 7,4','6,4 -> 2,0','0,9 -> 2,9','3,4 -> 1,4','0,0 -> 8,8','5,5 -> 8,2']

vents = []
for d in data:
	a, *_, b = d.split()
	a = [int(x) for x in a.split(',')]
	b = [int(x) for x in b.split(',')]
	vents.append([a,b])

def getEquation(x1,y1,x2,y2):
	if x1 != x2:
		a = (y1-y2)/(x1-x2)
		b = (x1*y2 - x2*y1)/(x1-x2)
		if y1 == a*x1+b and y2 == a*x2+b:
			return a, b
	else:
		return None, None

def getPoints(c1,c2):
	pts = []
	x1, y1 = c1
	x2, y2 = c2

	if x1 == x2:
		miny, maxy = min(y1,y2), max(y1,y2)
		for y in range(miny, maxy+1):
			pts.append((x1, y))
	else:
		a,b = getEquation(x1,y1,x2,y2)
		minx, maxx = min(x1,x2), max(x1,x2)
		for x in range(minx, maxx+1):
			pts.append((x, round(a*x+b)))
	return pts

def part1():
	coords = {}
	for v in vents:
		a, b = v
		if a[0] == b[0] or a[1] == b[1]:
			for p in getPoints(a,b):
				coords[p] = coords.get(p, 0) + 1
	ret = 0
	for c in coords:
		if coords[c] > 1:
			ret += 1
	return ret

def part2():
	coords = {}
	for v in vents:
			a, b = v
			for p in getPoints(a,b):
				coords[p] = coords.get(p, 0) + 1
	ret = 0
	for c in coords:
		if coords[c] > 1:
			ret += 1
	return ret

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
utils.evalTime(10,part1)
utils.evalTime(10,part2)