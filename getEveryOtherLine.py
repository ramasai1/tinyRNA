import sys
lc = 1
for line in sys.stdin:
	if lc == 1:
		print line[1: len(line) - 4]
		lc += 1
	else:
		lc = 1
