import utils
inputSeats = utils.getLinesFromFile("day11.input")

# inputSeats = ['L.LL.LL.LL','LLLLLLL.LL','L.L.L..L..','LLLL.LL.LL','L.LL.LL.LL','L.LLLLL.LL','..L.L.....','LLLLLLLLLL','L.LLLLLL.L','L.LLLLL.LL']

rows = len(inputSeats)
columns = len(inputSeats[1])
seats = [['.' for c in range(columns)] for r in range(rows)]

def getNextState(r, c, isPart2):
	# Part 1
	if not isPart2:
		adjacentOccupied = 0
		for i, j in [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]:
			if r+i >= 0 and c+j >= 0 and r+i < rows and c+j < columns:
				adjacentOccupied += (seats[r+i][c+j] == '#')
		if seats[r][c] == 'L' and not adjacentOccupied:
			return '#'
		elif seats[r][c] == '#' and adjacentOccupied >= 4:
			return 'L'
		return seats[r][c]
	# Part 2
	adjacentOccupied = 0
	for i, j in [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]:
		_r, _c = r+i, c+j
		foundOccupied = False
		while _r >= 0 and _c >= 0 and _r < rows and _c < columns and seats[_r][_c] != 'L' and not foundOccupied:
			foundOccupied = seats[_r][_c] == '#'
			_r, _c = _r+i, _c+j
		adjacentOccupied += foundOccupied
	if seats[r][c] == 'L' and not adjacentOccupied:
		return '#'
	elif seats[r][c] == '#' and adjacentOccupied >= 5:
		return 'L'
	return seats[r][c]

def play1Round(isPart2):
	_seats = [['.' for c in range(columns)] for r in range(rows)]
	for r in range(rows):
		for c in range(columns):
			if seats[r][c] != '.':
				_seats[r][c] = getNextState(r, c, isPart2)
	return _seats
def runUntilStop(isPart2):
	global seats
	for r in range(rows):
		seats[r] = [c for c in inputSeats[r]]
	stillChaos = True
	while stillChaos:
		_s = play1Round(isPart2)
		if seats == _s:
			stillChaos = False
		seats = _s

		cpt = 0
		for r in range(rows):
			cpt += seats[r].count('#')
			# print(''.join(seats[r]))
		# print()
	return cpt

# print(('Part 1'))
print(f'Part1: {runUntilStop(False)}')
# print()
# print(('Part 2'))
print(f'Part2: {runUntilStop(True)}')
	