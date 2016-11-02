import sys
import csv
linecount = 1
total = 0
lisum = []
line2 = ""
line1 = ""
templength = 0
histstats = {}
tenbp = []
elebp = []
twelbp = []
thirbp = []
fourbp = []
fifbp = []
sixbp = []
sevbp = []
eighbp = []
ninebp = []
twenbp = []
bplists = {'10' : tenbp, '11' : elebp, '12' : twelbp, '13' : thirbp, '14' : fourbp, '15' : fifbp, '16' : sixbp, '17' : sevbp, '18' : eighbp, '19' : ninebp, '20' : twenbp}


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
		if templength > 9 and templength < 21:
			bplists[str(templength)].append(line2)	
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

"""to measure diversity
for k in range(0,100):
	keylist = histstats[str(k)].keys()
	vallist = histstats[str(k)].values()
	print "read length: " + str(k)
	for l in range(0,len(keylist)):
		if vallist[l] >= (.05 * lisum[k]):
			print keylist[l],
			print str(vallist[l])
			print str(float(vallist[l])/float(lisum[k]) * 100)
"""
#bias on bases
print "Base Distribtion\n"
for m in range(10,21):
	templist = bplists[str(m)]
	gcounter = []
	ccounter = []
	acounter = []
	tcounter = []
	for init in range(0, m):
		gcounter.append(0)
		ccounter.append(0)
		acounter.append(0)
		tcounter.append(0)
	print "Read length: " + str(m)
	for n in range(0,len(templist)):	
		templine = templist[n]
		for o in range(0,len(templine)):
			if templine[o] == 'A':
				acounter[o] = acounter[o] + 1
			elif templine[o] == 'G':
				gcounter[o] = gcounter[o] + 1
			elif templine[o] == 'C':
				ccounter[o] = ccounter[o] + 1
			else: 
				tcounter[o] = tcounter[o] + 1	
	print "G"
	print gcounter
	print "A"
	print acounter
	print "T"
	print tcounter
	print "C"
	print ccounter	
