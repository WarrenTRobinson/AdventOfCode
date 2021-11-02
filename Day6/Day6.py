def count_yesses_part1(answers):
	yesses = set()
	for answer in answers: 
		for yes in answer:
			yesses.add(yes)
	return len(yesses)

def count_yesses_part2(answers):
	yesses = set()
	answers = [set(answer) for answer in answers]
	yesses = len(answers[0].intersection(*answers[1:]))
	return yesses

with open('input.txt') as f:
	answers = [line.strip() for line in f.readlines()]
	groups_answers = []
	total_yesses_part1 = 0
	total_yesses_part2 = 0

	for answer in answers:
		if answer == '':
			total_yesses_part1 += count_yesses_part1(groups_answers)
			total_yesses_part2 += count_yesses_part2(groups_answers)
			groups_answers = []
		else:
			groups_answers.append(answer)

	# the last group
	total_yesses_part1 += count_yesses_part1(groups_answers)
	total_yesses_part2 += count_yesses_part2(groups_answers)

	print('the answer to part one is {}'.format(total_yesses_part1))
	print('the answer to part two is {}'.format(total_yesses_part2))
