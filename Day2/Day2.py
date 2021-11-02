def parse_line(line):
	rules, password = line.strip().split(': ')
	rule_counts, rule_char = rules.split(' ')
	rule_counts = [int(count) for count in rule_counts.split('-')]
	return rule_counts, rule_char, password

def password_valid_part1(rule_counts, rule_char, password):
	rule_char_count = sum([1 if char == rule_char else 0 for char in password])
	return rule_char_count >= rule_counts[0] and rule_char_count <= rule_counts[1]

def password_valid_part2(rule_counts, rule_char, password):
	# logical xor: bool(a) != bool(b)
	return (password[rule_counts[0]-1] == rule_char) != (password[rule_counts[1]-1] == rule_char)


with open('input.txt') as f:
	part1_answer = 0
	part2_answer = 0
	lines = f.readlines()

	for line in lines:
		rule_counts, rule_char, password = parse_line(line)
		if password_valid_part1(rule_counts, rule_char, password):
			part1_answer += 1
		if password_valid_part2(rule_counts, rule_char, password):
			part2_answer += 1

	print('the answer to part one is {}'.format(part1_answer))
	print('the answer to part two is {}'.format(part2_answer))