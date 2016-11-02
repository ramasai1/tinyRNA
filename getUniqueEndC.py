import sys
import csv
from sets import Set
total = 0
linecount = 1
line2 = ""
line1 = ""
ten = Set([])
ele = Set([])
twe = Set([])
thi = Set([])
fou = Set([])
fif = Set([])
six = Set([])
sev = Set([])
eig = Set([])
nin = Set([])
twen = Set([])
mor = Set([])
nucs = 10
allsets = {'10': ten, '11': ele, '12': twe, '13': thi, '14': fou, '15': fif, '16': six, '17': sev, '18': eig, '19': nin, '20': twen, '21': mor}
dten = {}
dele = {}
dtwe = {}
dthi = {}
dfou = {}
dfif = {}
dsix = {}
dsev = {}
deig = {}
dnin = {}
dtwen = {}
dmor = {}
alldicts = {'10': dten, '11': dele, '12': dtwe, '13': dthi, '14': dfou, '15': dfif, '16': dsix, '17': dsev, '18': deig, '19': dnin, '20': dtwen, '21': dmor}

for line in sys.stdin: 
	if linecount == 1:
		line1 = line
	elif linecount == 2:
		line2 = line
		linecount = 0
		total = total + 1
		templine = line2.strip()
		upperline = templine.upper()
		templine = upperline
		if len(templine) > nucs:
			nucs = len(templine)
			if nucs > 20:
				nucs = 21
		if len(templine) == nucs or nucs == 21:
			if templine[nucs - 1] == 'c' or templine[nucs - 1] == "C":
				allsets[str(nucs)].add(templine)
				alldicts[str(nucs)][line1.strip()] = templine
	linecount = linecount + 1
#testing the app
substring = 0
removelines = Set([])

sizesets = {'10': len(allsets['10']), '11': len(allsets['11']), '12': len(allsets['12']), '13': len(allsets['13']), '14': len(allsets['14']), '15': len(allsets['15']), '16': len(allsets['16']), '17': len(allsets['17']), '18': len(allsets['18']), '19': len(allsets['19']), '20': len(allsets['20'])} 

#make the dictionary only have unique values
for uniq in range (10,21):
	t = [(k, alldicts[str(uniq)][k]) for k in alldicts[str(uniq)]]
	t.sort()
	alldicts[str(uniq)] = {}
	for k, v in t:
		if v not in alldicts[str(uniq)].values():
			alldicts[str(uniq)][k] = v
#remove substrings
for i in range (10, 21):
	for checkline in allsets[str(i)]:
		#want to check if checkline is a substring of larger sets
		for j in range(i + 1, 22):
			tempset = allsets[str(j)]
			#for each tempset, check if checkline exists
			for templine in tempset:
				if checkline in templine:
					substring = 1
					break
			else:
				continue
			if substring  == 1:
				break
		else: 
			continue
		if substring == 1:
			removelines.add(checkline)
			substring = 0
	newdict = {k: v for k, v in alldicts[str(i)].iteritems() if v not in removelines}
	removelines.clear()
	alldicts[str(i)] = {}
	alldicts[str(i)] = newdict
	newdict = {}
	for key, val in alldicts[str(i)].iteritems():
		print key
		print val
"""
f = open(line1[1:11] + ".csv", 'wt')
try:
	writer = csv.writer(f)
	for prints in range(10,21):
		writer.writerow((str(prints), str(sizesets[str(prints)] - len(alldicts[str(prints)])), len(alldicts[str(prints)])))
finally:
	f.close()
"""
