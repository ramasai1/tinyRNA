import sys
ncount = 0
total = 0
linecount = 1 #fastq format so four lines, only want second line
line1 = ""
line2 = ""
line3 = ""

for line in sys.stdin:

	if linecount == 1:
		line1 = line
	elif linecount == 2:
		line2 = line
	elif linecount == 3:
		line3 = line
	else:
		total = total + 1
		if "N" in line2:
			ncount = ncount + 1
		else:
			print line1,
			print line2,
			print line3,
			print line,
		linecount = 0
	
	linecount = linecount + 1
	
	

print "percent reads containing N: " + str(float(ncount)/float(total))
print "total reads containing N: " + str(ncount)
print "total reads: " + str(total)
