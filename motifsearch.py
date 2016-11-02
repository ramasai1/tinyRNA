import sys

lc = 1
line1 = ''
for line in sys.stdin:
	if lc == 1:
		line1 = line
	if lc == 2:
		if "TGGAAT" in line.strip():
			print line1,
			print line.strip()	
	if lc == 4:
		lc = 0
	lc += 1
