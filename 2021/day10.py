import utils
data = utils.getLinesFromFile("day10.input")

# data = ['[({(<(())[]>[[{[]{<()<>>','[(()[<>])]({[<{<<[]>>(','{([(<{}[<>[]}>{[]{[(<()>','(((({<>}<{<{<>}{[]{[]{}','[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]','{<[[]]>}<{[{[{[]{()[[[]','[<(<(<(<{}))><([]([]()','<{([([[(<>()){}]>(<<{{','<{([{{}}[<[[[<>{}]]]>[]]']

def part1():
	ret = 0
	equiv = {'{':'}', '(':')', '<':'>', '[':']'}
	pts = {')':3, ']':57, '}':1197, '>':25137}
	for d in data:
		stack = ''
		for i in d:
			if i in equiv:
				stack += i
			elif equiv[stack[-1]] == i:
				stack = stack[:-1]
			else:
				ret += pts[i]
				break
	return ret

def part2():
	ret = []
	equiv = {'{':'}', '(':')', '<':'>', '[':']'}
	pts = {')':1, ']':2, '}':3, '>':4}
	for d in data:
		stack = ''
		for i in d:
			if i in equiv:
				stack += i
			elif equiv[stack[-1]] == i:
				stack = stack[:-1]
			else:
				stack = ''
				break
		if len(stack) > 0:
			score = 0
			for i in stack[::-1]:
				score = score * 5 + pts[equiv[i]]
			ret.append(score)
	return sorted(ret)[round(len(ret)/2)-1] #for the example to work, remove this '-1'

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
