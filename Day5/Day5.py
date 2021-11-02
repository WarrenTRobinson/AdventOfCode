with open('input.txt') as f:
	boarding_pass_data = [line.strip() for line in f.readlines()]
	seat_IDs = []

	for boarding_pass in boarding_pass_data:
		row = boarding_pass[0:7]
		column = boarding_pass[7:]
		
		print(row)
		row = row.replace('F', '0').replace('B', '1')
		row = '0b' + row
		print(row)
		row = int(row, 2)
		print(row)

		column = column.replace('L', '0').replace('R', '1')
		column = '0b' + column
		column = int(column, 2)

		seat_IDs.append(row*8 + column)

	print('the answer to part 1 is {}'.format(max(seat_IDs)))

	every_seat_ID = list(range(max(seat_IDs)+1))
	missing_seats = [seat for seat in every_seat_ID if seat not in seat_IDs]

	print('the answer to part 2 is one of {}'.format(missing_seats))
