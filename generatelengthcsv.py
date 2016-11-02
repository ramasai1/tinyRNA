import sys
import copy
import csv
from sets import Set
headers = Set([])
linecount = 1
nucs = 10
line2 = ""
line1 = ""
counts = []
for count in range(0, 27):
	counts.append(0)

for line in sys.stdin:
	sample = line.strip()
	#fill in dictionaries for each read length
	dirname = '/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/'
	dirlist = [dirname + 'lengthcsv/afteradaptertrim/sorted/' + sample, dirname + 'lengthcsv/aftermaptogenome/sorted/' + sample, dirname + 'lengthcsv/afterremovemirna/sorted/' + sample, dirname + 'unique/' + sample]
	dicts = {}
	for fileparse in range(0, len(dirlist)):
		fileid = open(dirlist[fileparse], 'r')
		nucs = 10
		for line in fileid.readlines(): 
			if linecount == 1:
				line1 = line
			elif linecount == 2:
				line2 = line
				linecount = 0
				templine = line2.strip()
				if len(templine) > nucs:
					nucs = len(templine)
					if nucs > 25:
						nucs = 26
				if len(templine) == nucs or nucs == 26:
					counts[nucs] = counts[nucs] + 1
			linecount = linecount + 1
		fileid.close()
		dicts[str(fileparse)] = copy.copy(counts)
		for clear in range(0,27):
			counts[clear] = 0

	f = open(sample[1:10] + ".csv", 'wt')
	try:
		writer = csv.writer(f)
		writer.writerow(('Read length', 'After adapter trimming', 'After mapping to genome', 'After removing miRNA', 'After removing duplicates and substrings'))
		for prints in range(10, 26):
			writer.writerow((str(prints), dicts['0'][prints],  dicts['1'][prints], dicts['2'][prints],  dicts['3'][prints]))
	finally:
		f.close()
