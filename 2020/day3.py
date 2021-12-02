import utils

def countTrees(r, d):
	pattern = utils.getLinesFromFile("day3.input")
	trees = 0
	offset = 0

	for i in range(0, len(pattern), d):
		if pattern[i][offset] == '#':
			trees += 1
		offset += r
		offset %= len(pattern[i])
	return trees

print("Part1:",countTrees(3,1))
print("Part2:",countTrees(1,1)*countTrees(3,1)*countTrees(5,1)*countTrees(7,1)*countTrees(1,2))
