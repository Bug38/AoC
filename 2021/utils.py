def getIntsFromFile(filename):
	with open(filename, 'r') as f:
		return [int(x) for x in f]

def getLinesFromFile(filename):
	with open(filename, 'r') as f:
		return [x.strip() for x in f]

def evalTime(nbiter, func):
	import time
	start = time.time()
	for i in range(nbiter):
		func()
	print(f"Time for {nbiter} iteration{'s' if nbiter > 1 else ''}: {int((time.time() - start)*10000) / 10000}")
