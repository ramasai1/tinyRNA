import os
import sys
import csv
for line in sys.stdin:
	sample = line.strip()
	sample = sample[0:10] + '.sam'
	f = open("/cbcb/project-scratch/tinyRNAproj/Bowtie2/samfiles/" + sample, 'r')
	seqid = []
	mapqual = []
	read = []
	for sam in f.readlines():
		if 'SRR' in sam[0:3]:
			temp = sam.split()
			seqid.append(temp[0])
			mapqual.append(int(temp[4]))
			read.append(temp[9])	
	newfile = open(line[0:10] + '.txt', 'wt')

	for thing in mapqual:

		newfile.write(str(thing) + '\n')
	newfile.close()


	f.close()
	"""ten = []
	ele = []
	twe = []
	thi = []
	fou = []
	fif = []
	six = []
	sev = []
	eig = []
	nin = []
	twen = []
	twen1 = []
	twen2 = []
	twen3 = []	
	twen4 = []
	twen5 = []
	allsets = {'10': ten, '11': ele, '12': twe, '13': thi, '14': fou, '15': fif, '16': six, '17': sev, '18': eig, '19': nin, '20': twen, '21': twen1, '22' : twen2, '23' : twen3, '24' : twen4, '25' : twen5}
	for i in range(0, len(seqid)):
		temp = read[i].strip()
		length = len(temp)
		if length > 9 and length < 26:
			allsets[str(length)].append(mapqual[i])
	newfile = open(line[0:10] + '.csv', 'wt')
	writer = csv.writer(newfile)
	writer.writerow(ten)
	writer.writerow(ele)
	writer.writerow(twe)
	writer.writerow(thi)
	writer.writerow(fou)
	writer.writerow(fif)
	writer.writerow(six)
	writer.writerow(sev)
	writer.writerow(eig)
	writer.writerow(nin)
	writer.writerow(twen)
	writer.writerow(twen1)
	writer.writerow(twen2)
	writer.writerow(twen3)
	writer.writerow(twen4)
	writer.writerow(twen5)
	newfile.close()



"""
