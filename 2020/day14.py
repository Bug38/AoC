import utils
data = utils.getLinesFromFile("day14.input")

# data = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X','mem[8] = 11','mem[7] = 101','mem[8] = 0']
# data = ['mask = 000000000000000000000000000000X1001X','mem[42] = 100','mask = 00000000000000000000000000000000X0XX','mem[26] = 1']

def part1():
	memory = {}
	mask = '0'*36

	for d in data:
		address, value = 0,0
		if d[:4] == 'mask':
			mask = list(d[-36:])
		else:
			address, value = int(d.split('[')[1].split(']')[0]), list("{0:036b}".format(int(d.split('[')[1].split('=')[1])))
			for i in range(36):
				if mask[i] == 'X':
					continue
				value[i] = mask[i]
			if not address in memory:
				memory[address] = 0
			memory[address] = int(''.join(value),2)

	return sum([memory[m] for m in memory])


def part2():
	
	def getAdresses(base):
		addresses = []
		nbX = base.count('X')
		for i in range(pow(2,nbX)):
			ibin = f"{{0:0{nbX}b}}".format(i)
			ibinIndex = 0
			_a = list(base)
			for j in range(len(_a)):
				if _a[j] == 'X':
					_a[j] = ibin[ibinIndex]
					ibinIndex += 1
			addresses.append(''.join(_a))
		return addresses

	memory = {}
	mask = '0'*36

	for d in data:
		address, value = 0,0
		if d[:4] == 'mask':
			mask = d[-36:]
			_tmp = ''.join(mask)
		else:
			address, value = list("{0:036b}".format(int(d.split('[')[1].split(']')[0]))), int(d.split('[')[1].split('=')[1])
			_tmp = ''.join(address)
			for i in range(36):
				if mask[i] == '0':
					continue
				address[i] = mask[i]
			for a in getAdresses(''.join(address)):
				if not a in memory:
					memory[a] = 0
				memory[a] = value

	return sum([memory[m] for m in memory])


print(f'Part1: {part1()}')
print(f'Part2: {part2()}')