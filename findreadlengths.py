import sys
import csv
linecount = 1
total = 0
lisum = []
line2 = ""
line1 = ""
templength = 0
histstats = {}

for a in range(0,100):
	histstats[str(a)] = {}
	lisum.append(0)

for line in sys.stdin: 
	if linecount == 1:
		line1 = line
	elif linecount == 2:
		line2 = line
	elif linecount ==4:
		linecount = 0
		total = total + 1
		templength = len(line2)
		if histstats[str(templength)].has_key(line2):
			histstats[str(templength)][line2] = histstats[str(templength)][line2] + 1	
		else:
			histstats[str(templength)][line2] = 1	
	linecount = linecount + 1

f = open(line1[1:11] + ".csv", 'wt')
try:
	writer = csv.writer(f)
	for i in range(0,100):
		templist = histstats[str(i)].values()
		for j in range(0,len(templist)):
			lisum[i] = lisum[i] + templist[j]
		writer.writerow((str(i), lisum[i]))
finally:
	f.close()

#to measure diversity
for k in range(0,100):
	keylist = histstats[str(k)].keys()
	vallist = histstats[str(k)].values()
	print "read length: " + str(k)
	for l in range(0,len(keylist)):
		if vallist[l] >= (.05 * lisum[k]):
			print keylist[l],
			print str(vallist[l])
			print str(float(vallist[l])/float(lisum[k]) * 100)
