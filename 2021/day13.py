import utils
data = utils.getLinesFromFile("day13.input")

# data = ['6,10','0,14','9,10','0,3','10,4','4,11','6,0','6,12','4,1','0,13','10,12','3,4','3,0','8,4','1,10','2,14','8,10','9,0','','fold along y=7','fold along x=5']

dots = {}
for d in data[:data.index('')]:
	x,y = d.split(',')
	dots[(int(x), int(y))] = 1
inst = []
for d in data[data.index('')+1:]:
	axis, val = d.split()[-1].split('=')
	inst.append((axis, int(val)))
print(len(dots))

def printDots(dots):
	maxX, maxY = 0, 0
	for d in dots:
		x,y = d
		maxX, maxY = max(int(x), maxX), max(int(y), maxY)
	for y in range(maxY+1):
		line = ''
		for x in range(maxX+1):
			line += '█' if (x,y) in dots else ' '
		print(line)

def iterInst(i, dots):
	ret = {}
	axis, val = i
	for d in dots:
		x,y = d
		if axis == 'y' and y > val:
			ret[(x, y-2*(y-val))] = dots.get((x, y-2*(y-val)), 0) + dots[(x,y)]
		elif axis == 'x' and x > val:
			ret[(x-2*(x-val), y)] = dots.get((x-2*(x-val), y), 0) + dots[(x,y)]
		else:
			ret[(x,y)] = dots[(x,y)]
	return ret

def part1():
	d = dots.copy()
	for i in inst:
		d = iterInst(i, d)
		break
	return len(d)

def part2():
	d = dots.copy()
	for i in inst:
		d = iterInst(i, d)
	printDots(d)
	return len(d)

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
