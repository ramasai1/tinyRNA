import sys
line1 = ''
line2 = ''
linecount = 1
for line in sys.stdin:
	if linecount == 1:
		line1 = line.strip()
	else:
		tline = line.strip()
		line2 = tline.upper()
		print line1
		print line2
		linecount = 0	
	linecount = linecount + 1
