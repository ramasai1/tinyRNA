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
		if len(line2) == 30 and line2[20] == "T":
			print line1
			print line2[5:len(line2) - 5]
		linecount = 0	
	linecount = linecount + 1
