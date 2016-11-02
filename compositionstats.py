import sys
import csv
import os
linecount = 1
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
twen1bp = []
twen2bp = []
twen3bp = []
twen4bp = []
twen5bp = []

bplists = {'10' : tenbp, '11' : elebp, '12' : twelbp, '13' : thirbp, '14' : fourbp, '15' : fifbp, '16' : sixbp, '17' : sevbp, '18' : eighbp, '19' : ninebp, '20' : twenbp, '21' : twen1bp, '22' : twen2bp, '23' : twen3bp, '24' : twen4bp, '25' : twen5bp}

for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/15addedFastaNonLength/"):
	fastaid = open('/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/15addedFastaNonLength/' + file, 'r')
	for line in fastaid.readlines():
		if linecount == 1:
			linecount = 1
		elif linecount == 2:
			seq = line.strip()
			seq = seq.upper()
			if (len(seq) - 30) > 9 and (len(seq) - 30) < 26:
				bplists[str(len(seq) - 30)].append(seq)	
			linecount = 0
		linecount = linecount + 1
	#bias on bases
	for m in range(10,26):
		f = open(file[0:10] + '_' + str(m) + 'bp.csv', 'wt')
		writer = csv.writer(f)
		templist = bplists[str(m)]
		gcounter = []
		ccounter = []
		acounter = []
		tcounter = []
		for init in range(0, m + 30):
			gcounter.append(0)
			ccounter.append(0)
			acounter.append(0)
			tcounter.append(0)
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
		writer.writerow(acounter)
		writer.writerow(ccounter)
		writer.writerow(gcounter)
		writer.writerow(tcounter)
		f.close()
		bplists[str(m)] = []
	fastaid.close()
