import utils
data = utils.getLinesFromFile("day3.input")

# data = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

def getMostLess(list):
	most = [0]*len(list[0])
	for item in list:
		for i, letter in enumerate(item):
			if letter == '1':
				most[i] +=1
	for i in range(len(most)):
		most[i] = '1' if most[i] >= len(list)/2 else '0'
	most = ''.join(most)
	less = most.replace('0','.').replace('1','0').replace('.','1')
	return most, less

def part1():
	most, less = getMostLess(data)
	return int(most,2)*int(less,2)

def reduce(list, filter):
	l = []
	for j in range(len(list[0])):
		for i in range(len(list)):
			if list[i][j] == filter[j]:
				l.append(list[i])
	return l

def part2():
	oxygen = data.copy()
	for j in range(len(oxygen[0])):
		most, _ = getMostLess(oxygen)
		l = []
		for i in oxygen:
			if i[j] == most[j]:
				l.append(i)
		oxygen, l = l.copy(), []
		if len(oxygen) == 1:
			break
	co2 = data.copy()
	for j in range(len(co2[0])):
		most, _ = getMostLess(co2)
		l = []
		for i in co2:
			if i[j] != most[j]:
				l.append(i)
		co2, l = l.copy(), []
		if len(co2) == 1:
			break
	# print(oxygen, co2)
	return int(oxygen[0],2)*int(co2[0],2)

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
