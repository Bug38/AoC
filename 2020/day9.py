import utils
data = utils.getIntsFromFile("day9.input")
preambleLenght = 25

# data = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
# preambleLenght = 5

def getsums(ints):
	sums = []
	for i in range(len(ints)-1):
		for j in range(i+1, len(ints)):
			sums.append(ints[i]+ints[j])
	return sums

def getWeakness(weakData, target):
	for i in range(len(weakData)):
		sum = 0
		weakList = []
		while sum < target:
			sum += weakData[i]
			weakList.append(weakData[i])
			i += 1
		if sum == target:
			return min(weakList) + max(weakList)

for i in range(preambleLenght,len(data)):
	if not data[i] in getsums(data[i-preambleLenght:i]):
		print(f'Part1: {data[i]}')
		print(f'Part2: {getWeakness(data[:i], data[i])}')
		break
