import utils
bootCode = utils.getLinesFromFile("day8.input")

#bootCode = ['nop +0','acc +1','jmp +4','acc +3','jmp -3','acc -99','acc +1','jmp -4','acc +6']

def exec(codeLine, PC, accumulator):
	inst, value = codeLine.split()
	if inst == 'nop':
		PC += 1
		return PC, accumulator
	if inst == "acc":
		PC += 1
		accumulator += int(value)
		return PC, accumulator
	if inst == 'jmp':
		PC += int(value)
		return PC, accumulator

def execProgram(lineToChange):
	accumulator = 0
	PC = 0
	executedLines = []
	lowestLine = 0
	while (not PC in executedLines) and (PC <= len(bootCode) -1 ):
		executedLines.append(PC)
		if PC >= lowestLine:
			lowestLine = PC
		if lineToChange and PC == lineToChange:
			PC, accumulator = exec(bootCode[PC].replace('nop', 'nopReplace').replace('jmp', 'jmpReplace').replace('nopReplace', 'jmp').replace('jmpReplace', 'nop'), PC, accumulator)
		else:
			PC, accumulator = exec(bootCode[PC], PC, accumulator)
	return PC, accumulator

print(f'Part1: accumulator = {execProgram(None)[1]}')
for i in range(len(bootCode)):
	PC, accu = execProgram(i)
	if PC == len(bootCode):
		print(f'Part2: accumulator = {accu}')
		break