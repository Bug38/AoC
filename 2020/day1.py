import utils

target = 2020

expenses = utils.getIntsFromFile("day1.input")

# PART 1
for i in range(len(expenses)):
	for j in range(i,len(expenses)):
		if expenses[i]+expenses[j] == target:
			print("Part 1:",expenses[i]*expenses[j])
			break

# PART 2
for i in range(len(expenses)):
	for j in range(i,len(expenses)):
		for k in range(i,len(expenses)):
			if expenses[i]+expenses[j]+expenses[k] == target:
				print("Part 2:",expenses[i]*expenses[j]*expenses[k])
				exit()
