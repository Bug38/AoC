import utils
data = utils.getLinesFromFile("day13.input")

# data = ['939','7,13,x,x,59,x,31,19']
# data = ['939','17,x,13,19']
# data = ['939','67,7,59,61']
# data = ['939','67,x,7,59,61']
# data = ['939','67,7,x,59,61']
# data = ['939','1789,37,47,1889']

def part1():
	minDeparture = int(data[0])
	busIDs = []

	for b in data[1].split(','):
		if b == 'x':
			continue
		busIDs.append(int(b))
	
	deltaTime = max(busIDs)
	selectedBus = max(busIDs)
	for b in busIDs:
		_wait = b - (minDeparture % b)
		if _wait < deltaTime:
			deltaTime = _wait
			selectedBus = b
	
	return deltaTime * selectedBus

def part2():
	busIDs = []
	for b in data[1].split(','):
		if b == 'x':
			busIDs.append(0)
		else:
			busIDs.append(int(b))
	
	maxID = max(busIDs)
	maxIDindex = busIDs.index(maxID)
	
	pairs = []
	for i in range(len(busIDs)):
		if busIDs[i] == 0:
			continue
		pairs.append((busIDs[i], i - maxIDindex))

	iterator = 1
	for a,b in pairs:
		if a == b or a == -b or a == maxID:
			iterator *= a
			pairs.remove((a,b))

	nb = iterator
	while not all([(nb + b)% a == 0 for a,b in pairs]):
		nb += iterator
	
	return nb - maxIDindex

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')