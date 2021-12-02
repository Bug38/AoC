import utils
adapters = utils.getIntsFromFile("day10.input")

# adapters = [16,10,15,5,1,11,7,19,6,12,4]
# adapters = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]

outletJoltage = 0
deviceJoltage = max(adapters) + 3
adapters.append(outletJoltage)
adapters.append(deviceJoltage)
adapters.sort()

def part1():
	deltas = ['',0,0,0]
	for i in range(len(adapters)-1):
		deltas[adapters[i+1] - adapters[i]] += 1
	return deltas[1] * deltas[3]

multipliers = []

def getMultiplier(deltas):
	multipliers.append(len(deltas))
	if len(deltas) == 1:
		return 1
	if len(deltas) == 2:
		return 2
	if len(deltas) == 3:
		return 4
	if len(deltas) == 4:
		return 7
	if len(deltas) == 5:
		return 13
	if len(deltas) == 6:
		return 24
	return 1

def part2():
	deltaList = []
	for i in range(len(adapters)-1):
		deltaList.append(adapters[i+1] - adapters[i])
	arrangements = 1
	i = 0
	while i < len(deltaList) - 1:
		j = 1
		while i+j < len(deltaList)-1 and deltaList[i] == deltaList[i+j] and deltaList[i] != 3:
			j += 1
		arrangements *= getMultiplier(deltaList[i:i+j])
		i += j
	return arrangements

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')

# #4
# 1 1 1
# 2 1
# 1 2
# 3

# #7
# 1 1 1 1
# 2 1 1
# 1 2 1
# 1 1 2
# 3 1
# 1 3
# 2 2

# #10
# 1 1 1 1 1
# 2 1 1 1
# 1 2 1 1
# 1 1 2 1
# 1 1 1 2
# 2 2 1
# 2 1 2
# 1 2 2
# 3 1 1
# 1 3 1
# 1 1 3
# 3 2
# 2 3

# #24
# 1 1 1 1 1 1
# 2 1 1 1 1
# 1 2 1 1 1
# 1 1 2 1 1
# 1 1 1 2 1
# 1 1 1 1 2
# 2 2 1 1
# 2 1 2 1
# 2 1 1 2
# 1 2 2 1
# 1 2 1 2
# 1 1 2 2
# 2 2 2
# 3 1 1 1
# 1 3 1 1
# 1 1 3 1
# 1 1 1 3
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
# 3 3