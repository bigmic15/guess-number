import random

r = random.randint(1, 100)

while True:
	num = input('Please guess a number: ')
	num = int(num)

	if num == r:
		print('Bingo!')
		break
	elif num > r:
		print('Lower')
	elif num < r:
		print('Higher')
