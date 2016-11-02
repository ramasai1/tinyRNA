import sys

blah = {}
blah2 = {}
for line in sys.stdin:
	temp = line.strip().split()
	if len(temp[0]) == 1:
		blah[temp[1]] = temp[0]
	else:
		blah2[temp[1]] = temp[0]
for thing in sorted(blah2, key=blah2.get, reverse=True):
	print blah2[thing] + '\t' + thing
for thing in sorted(blah, key=blah.get, reverse=True):
	print blah[thing] + '\t' + thing
