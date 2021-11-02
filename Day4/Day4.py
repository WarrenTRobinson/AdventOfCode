def passport_valid_part1(passport):
	return ('byr' in passport and
		'iyr' in passport and 
		'eyr' in passport and
		'hgt' in passport and
		'hcl' in passport and
		'ecl' in passport and
		'pid' in passport)

def add_line_to_passport(line, passport):
	fields = line.split(' ')
	for field in fields: 
		key, val = field.split(':')
		passport[key] = val

def hcl_char_valid(c):
	return c >= 'a' and c <= 'f' or c >= '0' and c <= '9'

def passport_valid_part2(passport):
	byr = int(passport['byr'])
	if byr < 1920 or byr > 2002:
		return False

	iyr = int(passport['iyr'])
	if iyr < 2010 or iyr > 2020:
		return False

	eyr = int(passport['eyr'])
	if eyr < 2020 or eyr > 2030:
		return False

	hgt = passport['hgt']
	if hgt.endswith('cm'):
		hgt = int(hgt[0:-2])
		if hgt < 150 or hgt > 193:
			return False
	elif hgt.endswith('in'):
		hgt = int(hgt[0:-2])
		if hgt < 59 or hgt > 76:
			return False
	else: 
		return False

	hcl = passport['hcl']
	if hcl.startswith('#'):
		if len(hcl) != 7:
			return False
		for c in hcl[1:]:
			if not hcl_char_valid(c):
				return False
	else:
		return False

	ecl = passport['ecl']
	if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return False

	pid = passport['pid']
	if len(pid) != 9:
		return False

	return True


with open('input.txt') as f:
	passport_data = [line.strip() for line in f.readlines()]
	passport = {}
	answer_part1 = 0
	answer_part2 = 0

	for line in passport_data:
		if line == '':
			if passport_valid_part1(passport):
				answer_part1 += 1
				if passport_valid_part2(passport):
					answer_part2 += 1
					print(passport)
			passport = {}
		else:
			add_line_to_passport(line, passport)

    # the last passport
	if passport_valid_part1(passport):
		answer_part1 += 1
		if passport_valid_part2(passport):
			answer_part2 += 1
			print(passport)

	print('the answer to part one is {}'.format(answer_part1))
	print('the answer to part two is {}'.format(answer_part2))
