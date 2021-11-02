import itertools

with open('input') as f:
	answer = None
	data = [int(line) for line in f.readlines()]
	for r in itertools.product(data, data):
		if r[0] + r[1] == 2020:
			answer = r[0] * r[1]
			break

	print('the answer to part one is {}'.format(answer))

	for r in itertools.product(data, data, data):
		if r[0] + r[1] + r[2] == 2020:
			answer = r[0] * r[1] * r[2]
			break

	print('the answer to part two is {}'.format(answer))


	