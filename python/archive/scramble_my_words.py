import random

while True:
	text = input('What do you want to scramble?: ')
	_new = text.split(' ')
	random.shuffle(_new)
	print('')
	print(' '.join(_new), end='\n\n')
