import random
import cmd 

def arrival1(n=8):
	while True:
		yield random.randrange(n)

def samples(limit, generator):
	for n, value in enumerate(generator):
		if n == limit: break
		yield value

random.seed(1)
list(samples(10, arrival1()))