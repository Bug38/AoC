import utils

passwords = utils.getLinesFromFile("day2.input")

okPwdPart1 = []
okPwdPart2 = []

# PART 1
for p in passwords:
	limits, letter, pwd = p.split()
	limits = [int(x) for x in limits.split('-')]
	#print(limits, letter, pwd)
	nb = pwd.count(letter[0])
	if nb <= limits[1] and nb >= limits[0]:
		okPwdPart1.append(p)
print("Part 1:", len(okPwdPart1))


# PART 2
for p in passwords:
	pos, letter, pwd = p.split()
	pos = [int(x) for x in pos.split('-')]
	nb = (pwd[pos[0] -1] == letter[0]) + (pwd[pos[1] -1] == letter[0])
	if nb == 1:
		okPwdPart2.append(p)
print("Part 2:", len(okPwdPart2))


