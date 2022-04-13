import random
def coin_flip():
	return random.choice(['heads', 'tails'])

if coin_flip() == 'heads':
	print('Heads!')
else:
	print('Tails!')