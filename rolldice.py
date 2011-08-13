#! /usr/bin/env python3

# run it like:
# rolldice 2d20
# WARNING: bad input is not handled

from random import randint
from sys import argv

if len(argv) < 2:
	print("must have an argument, ie 2d20")
	exit(1)
args = [int(i) for i in argv[1].split('d')]
print(sum(randint(1,args[1]) for i in range(args[0])))

