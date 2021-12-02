import utils

rules = utils.getLinesFromFile("day7.input")

bagTypes = []

_r = {}
for r in rules:
	color, content = ' '.join(r.split()[:2]), ' '.join(r.split()[4:]).replace('.', '').split(',')
	if content[0] != 'no other bags':
		_c = {}
		for c in content:
			nb, bagColor = c.split()[0], ' '.join(c.split()[1:-1])
			_c[bagColor] = int(nb)
		content = _c
	#print(color, '-->', content)
	_r[color] = content
rules = _r

# print(rules)
def getBagsInBag(bagColor, color):
	# print(bagColor, color)
	count = 0
	if color:
		if bagColor:
			if rules[bagColor] == ['no other bags']:
				return 0
			for c in rules[bagColor]:
				if c == color:
					count += rules[bagColor][color]
				else:
					count += getBagsInBag(c, color)
			return count
		for c in rules:
			if c == color:
				None
			else:
				count += getBagsInBag(c, color)
		return count
	if bagColor:
		if rules[bagColor] == ['no other bags']:
			return 1
		for c in rules[bagColor]:
			count += rules[bagColor][c] * getBagsInBag(c, color)
		return 1 + count
	for c in rules:
		count += getBagsInBag(c, color)
	return count
		

# print(getBagsInBag(None, 'shiny gold'))

nbBags1=0
for b in rules:
	if getBagsInBag(b, 'shiny gold'):
		nbBags1 += 1

print(f"Part 1: {nbBags1}")
print(f"Part 2: {getBagsInBag('shiny gold', None) - 1}")

# def getBagRule(b):
# 	r= {}
# 	return {}