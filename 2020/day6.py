import utils

yesCount1 = 0
yesCount2 = 0
groupcount1 = []
groupcount2 = []


for a in utils.getLinesFromFile("day6.input"):
	if len(a) == 0:
		yesCount1 += len(groupcount1)
		yesCount2 += len(groupcount2)
		groupcount1 = []
		groupcount2 = []
		continue
	if len(groupcount1) == 0:
		groupcount2 = set(a)
	else:
		groupcount2 = groupcount2&set(a)
	for l in a:
		if not l in groupcount1:
			groupcount1.append(l)
# last line
yesCount1 += len(groupcount1)
yesCount2 += len(groupcount2)

print(f"Part 1: {yesCount1}")
print(f"Part 2: {yesCount2}")
