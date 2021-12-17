from typing import Set
import utils
data = utils.getLinesFromFile("day8.input")

# data = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe','edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc','fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg','fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb','aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea','fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb','dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe','bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef','egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb','gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce']
# data = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']

inputs, outputs = [], []
for d in data:
	a, b = d.split('|')
	inputs.append(a.strip().split())
	outputs.append(b.strip().split())

def part1():
	ret = 0
	for os in outputs:
		for o in os:
			if len(o) in [2, 3, 4, 7]:
				ret += 1
	return ret

def part2():
	ret = 0
	for i, ins in enumerate(inputs):
		ins = sorted(ins, key=len)
		wires = [0, ins[0], 0, 0, ins[2], 0, 0, ins[1], ins[-1], 0]
		for w in ins:
			if len(w) in [2, 3, 4, 7]:
				continue
			if len(w) == 5 and set(wires[1]).issubset(set(w)):
				wires[3] = w
				continue
			if len(w) == 6 and set(wires[3]).issubset(set(w)):
				wires[9] = w
				continue
			elif len(w) == 6 and set(wires[1]).issubset(set(w)):
				wires[0] = w
				continue
			elif len(w) == 6:
				wires[6] = w
				continue
		for w in ins:
			if w in wires:
				continue
			if set(w).issubset(set(wires[6])):
				wires[5] = w
			else:
				wires[2] = w
		value = ""
		for o in outputs[i]:
			for i, w in enumerate(wires):
				if set(o) == set(w):
					value += str(i)
					break
		ret += int(value)
	return ret

print(f'Part1: {part1()}')
print(f'Part2: {part2()}')
