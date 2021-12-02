import utils

lines = utils.getLinesFromFile("day4.input")

def getPassports(l):
	p = []
	_p = {}
	for _l in l:
		if not len(_l):
			if len(_p):
				p.append(_p)
				_p = {}
		for e in _l.split():
			k,v = e.split(':')
			_p[k] = v
	if len(_p):
		p.append(_p)
		_p = {}
	return p

def isValid(p, securityLevel):
	if securityLevel == 1:
		if len(p) == 8:
			return True
		else:
			if len(p) == 7 and not 'cid' in p:
				return True
		return False
	if securityLevel == 2:
		if not isValid(p, 1):
			return False
		if int(p["byr"]) < 1920 or int(p["byr"]) > 2002:
			return False
		if int(p["iyr"]) < 2010 or int(p["iyr"]) > 2020:
			return False
		if int(p["eyr"]) < 2020 or int(p["eyr"]) > 2030:
			return False
		try:
			_unit = p["hgt"][-2:]
			_value = int(p["hgt"][:-2])
			assert((_value >= 150 and _value <= 193) if _unit == "cm" else ((_value >=  59 and _value <=  76) if _unit == "in" else False))
		except:
			return False
		try:
			assert(p["hcl"][0] == '#')
			assert(len(p["hcl"]) == 7)
			_ = int(p["hcl"][1:],16)
		except:
			return False
		if not p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
			return False
		if len(p["pid"]) != 9 or p["pid"].lower() != p["pid"].upper():
			return False
		return True

		

passports = getPassports(lines)
valids = 0

print("Part 1:", sum([isValid(p, 1) for p in passports]))
print("Part 2:", sum([isValid(p, 2) for p in passports]))