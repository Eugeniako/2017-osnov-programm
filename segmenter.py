import sys


ss = sys.stdin.readlines()

for line in ss:
	y = line.replace("з.д.", 'ррам')
	x = y.replace("с. ш. ", 'oiu')
	h = x.replace(".",".\n")
	d = h.replace('ррам', "з.д")
	f = d.replace('oiu', "с. ш. ")
	print(f)
