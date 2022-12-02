from collections import Counter
import utils
data = utils.getLinesFromFile("day14.input")

# data = ['NNCB','','CH -> B','HH -> N','CB -> H','NH -> C','HB -> C','HC -> B','HN -> C','NN -> C','BH -> H','NC -> B','NB -> B','BN -> B','BB -> N','BC -> B','CC -> N','CN -> C']

rules = {}
for d in data[2:]:
	pair, _, new = d.split()
	rules[pair] = new

def part1():
	polymer = data[0]
	for _ in range(10):
		newP = ''
		for i in range(len(polymer)-1):
			newP = newP + polymer[i] + rules[polymer[i:i+2]]
		newP += polymer[-1]
		polymer = newP
	cpt = Counter(polymer)
	return cpt[max(cpt, key=cpt.get)] - cpt[min(cpt, key=cpt.get)]

def part2():
	polymer = {}
	for i in range(len(data[0]) - 1):
		polymer[data[0][i:i+2]] = polymer.get(data[0][i:i+2], 0) + 1
	for _ in range(40):
		newP = {}
		for k in polymer:
			newk = [k[0] + rules[k], rules[k] + k[1]]
			for i in newk:
				newP[i] = newP.get(i, 0) + polymer[k]
		polymer = newP
	cpt = {}
	for k in polymer:
		cpt[k[0]] = cpt.get(k[0], 0) + polymer[k]
	cpt[data[0][-1]] = cpt.get(data[0][-1], 0) + 1
	return cpt[max(cpt, key=cpt.get)] - cpt[min(cpt, key=cpt.get)]

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
