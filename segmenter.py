import sys


ss = sys.stdin.readlines()

for line in ss:
	h = line.replace(".",".\n")
	print(h)
