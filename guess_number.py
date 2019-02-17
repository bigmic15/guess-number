import random

start_num = input('Please enter a start number: ')
end_num = input('Please enter an end number: ')

start_num = int(start_num)
end_num = int(end_num)


r = random.randint(start_num, end_num)

count_attempt = 0

while True:
	count_attempt += 1 # count_attempt = count_attempt + 1
	num = input('Please guess a number: ')
	num = int(num)

	if num == r:
		print('Bingo!')
		if count_attempt == 1:
			print(count_attempt, 'attempt')
		else:
			print(count_attempt, 'attempts')
		break
	elif num > r:
		print('Lower')
	elif num < r:
		print('Higher')

	if count_attempt == 1:
		print(count_attempt, 'attempt')
	else:
		print(count_attempt, 'attempts')