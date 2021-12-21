import utils
data = utils.getLinesFromFile("day12.input")

# data = ['start-A','start-b','A-b','A-c','b-d','A-end','b-end']
# data = ['dc-end','HN-start','start-kj','dc-start','dc-HN','LN-dc','HN-end','kj-sa','kj-HN','kj-dc']

paths = {}
bigCaves = set()
for d in data:
	f, t = d.split('-')
	paths[f] = paths.get(f,[]) + [t]
	paths[t] = paths.get(t,[]) + [f]
	if f.isupper():
		bigCaves.add(f)
	if t.isupper():
		bigCaves.add(t)

def twice(path):
	nodes = {}
	for r in path:
		nodes[r] = nodes.get(r, 0) + 1
		if nodes[r] > 1 and not r in bigCaves:
			return True
	return False

def listpaths(currL, part2):
	l = []
	for d in paths[currL[-1]]:
		if d == 'end':
			l.append([d, "twice"])
			continue
		if d in currL and not d in bigCaves:
			if not part2 or d == 'start' or (part2 and twice(currL)):
				continue
		_p = listpaths(currL + [d], part2)
		for _l in _p:
			l.append([d] + _l)
	return l

def part1():
	return len(listpaths(['start'], False))

def part2():
	return len(listpaths(['start'], True))


print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
