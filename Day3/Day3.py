tree = '#'

def count_trees_with_slope(x, y, data):
	right_index = 0
	tree_count = 0

	for i, line in enumerate(data[x:]):
		if i % x != 0:
			continue 
		right_index += y
		tree_location = right_index % len(line)
		if line[tree_location] == tree:
			tree_count += 1

	return tree_count

with open('input.txt') as f:
	data = [line.strip() for line in f.readlines()]
	right_index = 0
	answer_part1 = count_trees_with_slope(1, 3, data)
	answer_slope1 = count_trees_with_slope(1, 1, data)
	answer_slope2 = answer_part1
	answer_slope3 = count_trees_with_slope(1, 5, data)
	answer_slope4 = count_trees_with_slope(1, 7, data)
	answer_slope5 = count_trees_with_slope(2, 1, data)
	answer_part2 = answer_slope1 * answer_slope2 * answer_slope3 * answer_slope4 * answer_slope5

	print('the answer to part 1 is {}'.format(answer_part1))
	print('the answer to part 2 is {}'.format(answer_part2))