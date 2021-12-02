import utils
data = utils.getLinesFromFile("day16.input")

# data = ['class: 1-3 or 5-7','row: 6-11 or 33-44','seat: 13-40 or 45-50','','your ticket:','7,1,14','','nearby tickets:','7,3,47','40,4,50','55,2,20','38,6,12']

rules = {}
tickets = []
ownTicket = []

for d in data[:data.index('')]:
	rules[d.split(':')[0]] = [[int(x) for x in d.split(" ")[-3].split("-")], [int(x) for x in d.split(" ")[-1].split("-")]]

ownTicket = [int(x) for x in data[data.index('')+2].split(',')]

for d in data[data.index('', data.index('')+1)+2:]:
	tickets.append([int(x) for x in d.split(',')])


def part1():
	validValues = []
	for r in rules:
		for i in list(range(rules[r][0][0], rules[r][0][1]+1))+list(range(rules[r][1][0], rules[r][1][1]+1)):
			validValues.append(i)

	invalids = []
	for t in tickets:
		for v in t:
			if not v in validValues:
				invalids.append(v)
	return invalids

def part2():
	def sortFields(fields):
		while 1:
			needsAnotherRun = False
			for f in fields:
				if len(fields[f]) == 1:
					for _f in fields:
						if f == _f:
							continue
						if fields[f][0] in fields[_f]:
							fields[_f].remove(fields[f][0])
							needsAnotherRun = True
			if not needsAnotherRun:
				return fields

	invalids = set(part1())
	valids = []
	for t in tickets:
		if set(t) & invalids:
			continue
		valids.append(t)
	valids.append(ownTicket)
	fields = {}
	for r in rules:
		fields[r] = []
		for i in range(len(valids[0])):
			stillValid = True
			for v in valids:
				if not ((rules[r][0][0] <= v[i] and v[i] <= rules[r][0][1]) or (rules[r][1][0] <= v[i] and v[i] <= rules[r][1][1])):
					stillValid = False
					break
			if stillValid:
				fields[r].append(i)
	fields = sortFields(fields)
	ret = 1
	for f in fields:
		if f[:9] == "departure":
			ret *= ownTicket[fields[f][0]]
	return ret
		

print(f'Part1: {sum(part1())}')
print(f'Part2: {part2()}')