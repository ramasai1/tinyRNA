import sys

lc = 1
line1 = ''
correct = "TGGAAT"
for line in sys.stdin:
	if lc == 1:
		line1 =  line.strip()[1:]
	else:
		temp = line.strip().upper()
		motif = temp[len(temp) - 15 : len(temp) - 9]
		hd = 0
		for i in range(0, len(motif)):
			if motif[i] != correct[i]:		
				hd += 1
		if hd < 2:
			print line1
	
		else:
			line1 = ''
		lc = 0
	lc += 1
