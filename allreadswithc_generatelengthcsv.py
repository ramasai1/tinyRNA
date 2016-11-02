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
for count in range(0, 22):
	counts.append(0)

#fill in dictionaries for each read length
dirname = '/cbcb/project-scratch/tinyRNAproj/DEMO/'
dirlist = [dirname + 'splitsamples/sortSRR3279553.fa', dirname + 'Nremoved/sortSRR3279553.fa', dirname + 'finalClipped/sortSRR3279553.fa', dirname + 'bowtie/bedoutput/sortSRR3279553.fa', dirname + 'bowtie/mirnaremovedbed/sortSRR3279553.fa', dirname + 'unique10to20/SRR3279553.fa']
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
				if nucs > 20:
					nucs = 21
			if len(templine) == nucs or nucs == 21:
				counts[nucs] = counts[nucs] + 1
		linecount = linecount + 1
	fileid.close()
	dicts[str(fileparse)] = copy.copy(counts)
	for clear in range(0,22):
		counts[clear] = 0

f = open("combined.csv", 'wt')
try:
	writer = csv.writer(f)
	writer.writerow(('Read length', 'Starting FASTQ', 'After N removal', 'After adapter trimming', 'After mapping to genome', 'After removing miRNA', 'After removing duplicates and substrings'))
	for prints in range(10, 21):
		writer.writerow((str(prints), dicts['0'][prints],  dicts['1'][prints], dicts['2'][prints],  dicts['3'][prints],  dicts['4'][prints],  dicts['5'][prints]))
finally:
	f.close()
