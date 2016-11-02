import os
from os.path import join as pjoin
import sys
import csv
#feed in txt file of sample names
for line in sys.stdin:
	path_to_file = pjoin("/cbcb", "project-scratch", "tinyRNAproj", "samples", "FINALSAMPLES", "GENICBIASRESULTS", line[0:10] + '.csv')
	newfile = open(path_to_file, "wt")
	writer = csv.writer(newfile)

	#store the count arrays for each region
	threeprime = []
	fiveprime = []
	exons = []
	introns = []
	upstream = []
	downstream = []
	intergenic = []
	for i in range(0, 28):
		threeprime.append(0.0)
		fiveprime.append(0.0)
		exons.append(0.0)
		introns.append(0.0)
		upstream.append(0.0)
		downstream.append(0.0)
		intergenic.append(0.0)

	alldicts = {'3primeremoved' : threeprime, '5primeremoved' : fiveprime, 'exonremoved' : exons, 'intronremoved' : introns, 'upstream' : upstream, 'downstream' : downstream, 'intergenic' : intergenic}
	
	for region in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/GENICBIAS/"):
		counts = []
		for i in range(0,28):		
			counts.append(0)
		for length in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/GENICBIAS/3primeremoved/"):
			beforeremove = open("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/bylengths/bedfiles/" + length + "/" + line[0:10] + ".bed")
			afterremove = open("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/GENICBIAS/" + region + "/" + length + "/" + line[0:10] + ".bed")
			before = 0
			after = 0
			for l in beforeremove.readlines():
				before = before + 1	
			for m in afterremove.readlines():
				after = after + 1
			if length != "13c" and length != "20plus1t":
				if before == 0:
					counts[int(length)] = 0.0
				else:
					counts[int(length)] = (before - after)/float(before)
			elif length == "13c":
				if before == 0:
					counts[26] = 0.0
				else:
					counts[26] = (before - after)/float(before)
			else:
				if before == 0:
					counts[27] = 0.0
				else:
					counts[27] = (before - after)/float(before)
		for j in range(0, 28):
			alldicts[region][j] = counts[j]
	for k in range(10, 28):
		alldicts['intergenic'][k] = 1 - (alldicts['3primeremoved'][k] + alldicts['5primeremoved'][k] + alldicts['exonremoved'][k] + alldicts['intronremoved'][k] + alldicts['upstream'][k] + alldicts['downstream'][k])
		if alldicts['intergenic'][k] < 0.0:
			alldicts['intergenic'][k] = 0.0
	writer.writerow(alldicts['3primeremoved'])
	writer.writerow(alldicts['5primeremoved'])
	writer.writerow(alldicts['exonremoved'])
	writer.writerow(alldicts['intronremoved'])
	writer.writerow(alldicts['upstream'])
	writer.writerow(alldicts['downstream'])
	writer.writerow(alldicts['intergenic'])
	newfile.close()
