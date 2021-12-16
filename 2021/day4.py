import utils, copy
data = utils.getLinesFromFile("day4.input")

# data = [
# '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
# '',
# '22 13 17 11  0',
# ' 8  2 23  4 24',
# '21  9 14 16  7',
# ' 6 10  3 18  5',
# ' 1 12 20 15 19',
# '',
# ' 3 15  0  2 22',
# ' 9 18 13 17  5',
# '19  8  7 25 23',
# '20 11 10 24  4',
# '14 21 16 12  6',
# '',
# '14 21 17 24  4',
# '10 16 15  9 19',
# '18  8 23 26 20',
# '22 11 13  6  5',
# ' 2  0 12  3  7',
# ]

numbers = [int(x) for x in data[0].split(',')]
grids = []

_d = []
for d in data[2:]:
	_d.append([int(x) for x in d.split()])
data = _d

for i in range(0,len(data),6):
	grids.append(data[i:i+5])


def hasGridWon(g):
	for l in g:
		if l == [None] * len(l):
			return True
	for i in range(len(g[0])):
		if [g[x][i] for x in range(len(g))] == [None] * len(l):
			return True
	return False

def sumGrid(g):
	s = 0
	for l in g:
		for n in l:
			s += n or 0
	return s

def iterGrid(g):
	for n in numbers:
		for l in g:
			if n in l:
				l[l.index(n)] = None
		if hasGridWon(g):
			return numbers.index(n)

def part1():
	part1Grids = copy.deepcopy(grids)
	res = []
	for g in part1Grids:
		res.append(iterGrid(g))
	return numbers[min(res)] * sumGrid(part1Grids[res.index(min(res))])

def part2():
	part2Grids = copy.deepcopy(grids)
	res = []
	for g in part2Grids:
		res.append(iterGrid(g))
	return numbers[max(res)] * sumGrid(part2Grids[res.index(max(res))])


print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
