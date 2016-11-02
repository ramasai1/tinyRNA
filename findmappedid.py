import sys

for line in sys.stdin:
	strlist = line.split()
	mappedid = strlist[3]
	
	print mappedid
