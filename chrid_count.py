import sys
temp = {}
for line in sys.stdin:
	splitter = line.split()
	if splitter[0] not in temp:
		temp[splitter[0]] = 0
	else:
		temp[splitter[0]] += 1
for thing in temp:
	print 'Position was mapped to: ' + str(thing) + ' times, by: ' + str(temp[thing]) + ' many sequences'
