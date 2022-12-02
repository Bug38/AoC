input = open("01/01.txt").readlines()

input2 = ["1000",
"2000",
"3000",
"",
"4000",
"",
"5000",
"6000",
"",
"7000",
"8000",
"9000",
"",
"10000"]


part1 = 0
current = 0
elves = []

for l in input:
    if l.strip() == "":
        part1 = max(current, part1)
        elves.append(current)
        current = 0
        continue
    current += int(l)

part2 = sum(sorted(elves)[-3:])

print(f'{part1=}')
print(f'{part2=}')
print()