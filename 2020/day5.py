import utils

boardingPasses = utils.getLinesFromFile("day5.input")

def getPlace(bp):
	bp = bp.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
	return int(bp, 2)

boardingPasses = sorted([getPlace(x) for x in boardingPasses])

print(f"Part 1: {max(boardingPasses)}")
print(f"Part 2: {sorted(set(range(boardingPasses[0], boardingPasses[-1])) - set(boardingPasses))[0]}")