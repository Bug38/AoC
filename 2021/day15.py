from copy import deepcopy
import utils
data = utils.getLinesFromFile("day15.input")

# data = ['1163751742','1381373672','2136511328','3694931569','7463417111','1319128137','1359912421','3125421639','1293138521','2311944581']

data = [[int(x) for x in data[y]] for y in range(len(data))]

# map = [[int(x) for x in d] for d in data]
map = {}
def createMap(d):
	global map
	for y in range(len(d)):
		for x in range(len(d[0])):
			map[(x,y)] = d[y][x]

class Node:
	def __init__(self, parent=None, position=None):
		self.parent = parent
		self.position = position
		self.g = 0
		self.h = 0
		self.f = 0
	def __eq__(self, n):
		return self.position == n.position
	def __repr__(self):
		return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"
	def getPos(self):
		return self.position
	def getf(self):
		return self.f

def getChilds(c):
	x, y = c
	ret = []
	for xx, yy in [[0,-1],[-1,0],[0,1],[1,0]]:
		if (x+xx,y+yy) in map:
			ret.append((x+xx,y+yy))
	return ret

def Astar(targetPos):
	openlist = []
	closedlist = []
	start = (0,0)
	startN = Node(None, start)
	endN = Node(None, targetPos)

	openlist.append(startN)
	while len(openlist):
		currN = sorted(openlist, key=Node.getf)[0]
		# print(currN)
		openlist.remove(currN)
		closedlist.append(currN)
		if currN == endN:
			path = []
			while currN is not None:
				path.append(currN.position)
				currN = currN.parent
			return path[::-1]
		for c in getChilds(currN.getPos()):
			if len([cc for cc in closedlist if cc.position == c]):
				continue
			c = Node(currN, c)
			c.g = c.parent.g + map[c.position]
			c.h = abs(endN.position[0] - c.position[0]) + abs(endN.position[1] - c.position[1])
			c.f = c.g + c.h
			if len([n for n in openlist if n.position == c.position and c.g >= n.g]):
				continue
			openlist.append(c)
			# print(c)




def part1():
	createMap(data)
	path = Astar((len(data)-1, len(data[0])-1))
	return sum([map[c] for c in path[1:]])

def part2():
	newData = deepcopy(data)
	for i in range(4):
		for y in range(len(newData)):
			for _ in range(len(data[y])):
				n = newData[y][-len(data[y])] + 1
				n = n - 9 if n > 9 else n
				newData[y].append(n)
	for i in range(4):
		d = []
		for y in range(len(data)):
			d.append([])
			for x in range(len(newData[0])):
				n = newData[y-len(data)][x] + 1
				n = n - 9 if n > 9 else n
				d[y].append(n)
		newData += d

	createMap(newData)
	path = Astar((len(newData)-1, len(newData[0])-1))
	return sum([map[c] for c in path[1:]])

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
