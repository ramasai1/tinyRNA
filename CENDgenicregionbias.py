import os
import csv
direc = "/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/"
for file in os.listdir(direc + "NONCEND_gregremoved_sortedfasta/3prime/"):
	temp = open(direc +  "NONCEND_gregremoved_sortedfasta/3prime/" + file, 'r')
	noncremoved3prime = temp.readlines()
	temp.close()
	
	temp = open(direc +  "NONCEND_gregremoved_sortedfasta/5prime/" + file, 'r')
	noncremoved5prime = temp.readlines()
	temp.close()

	temp = open(direc +  "NONCEND_gregremoved_sortedfasta/exon/" + file, 'r')
	noncremovedexon = temp.readlines()
	temp.close()

	temp = open(direc +  "NONCEND_gregremoved_sortedfasta/intron/" + file, 'r')
	noncremovedintron = temp.readlines()
	temp.close()
	
	temp = open(direc +  "CEND_gregremoved_sortedfasta/3prime/" + file, 'r')
	cremoved3prime = temp.readlines()
	temp.close()
	
	temp = open(direc +  "CEND_gregremoved_sortedfasta/5prime/" + file, 'r')
	cremoved5prime = temp.readlines()
	temp.close()

	temp = open(direc +  "CEND_gregremoved_sortedfasta/exon/" + file, 'r')
	cremovedexon = temp.readlines()
	temp.close()

	temp = open(direc +  "CEND_gregremoved_sortedfasta/intron/" + file, 'r')
	cremovedintron = temp.readlines()
	temp.close()
	
	temp = open(direc +  "lengthcsv/afterremovedup/" + file, 'r')
	beforenoncremoved = temp.readlines()
	temp.close()

	temp = open(direc +  "uniqueEndC/" + file, 'r')
	beforecremoved = temp.readlines()
	temp.close()

	allfiles = [noncremoved3prime, noncremoved5prime, noncremovedexon, noncremovedintron, cremoved3prime, cremoved5prime, cremovedexon, cremovedintron, beforenoncremoved, beforecremoved]
	counts = [[] for some in range(len(allfiles))]
	
	for i in range(0, len(allfiles)):
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
		bplists = {'10' : tenbp, '11' : elebp, '12' : twelbp, '13' : thirbp, '14' : fourbp, '15' : fifbp, '16' : sixbp, '17' : sevbp, '18' : eighbp, '19' : ninebp, '20' : twenbp}


		for init in range(0, 21):
			counts[i].append(0)
		for line in allfiles[i]:
			if linecount == 1:
				linecount = 1
			elif linecount == 2:
				seq = line.strip()
				seq = seq.upper()
				if (len(seq) > 9) and (len(seq) < 21):
					bplists[str(len(seq))].append(seq)
				linecount = 0
			linecount = linecount + 1
		for j in range(10, 21):
			counts[i][j] = len(bplists[str(j)])

#now, we have the list of lists counts, which for each file, has the distribution of reads of len 10 to 20

	#using counts, we have to find out what fraction of each reads of each length before removal, was comprised of one of the four regions
	#nonc
	threeprime = []
	fiveprime = []
	exons = []
	introns = []
	remainder = []
	for sub in range(0,21):
		threeprime.append(0)
		fiveprime.append(0)
		exons.append(0)
		introns.append(0)
		remainder.append(0)
	for sub1 in range(0,21):
		if (sub1 < 10):
			threeprime[sub1] = 0
			fiveprime[sub1] = 0
			exons[sub1] = 0
			introns[sub1] = 0
			remainder[sub1] = 0
		else: 
			threeprime[sub1] = float((counts[9][sub1] - counts[4][sub1])) / float(counts[9][sub1])
			fiveprime[sub1] = float((counts[9][sub1] - counts[5][sub1])) / float(counts[9][sub1])
			exons[sub1] = float((counts[9][sub1] - counts[6][sub1])) / float(counts[9][sub1])
			introns[sub1] = float((counts[9][sub1] - counts[7][sub1])) / float(counts[9][sub1])
			remainder[sub1] = 1 - (threeprime[sub1] + fiveprime[sub1] + exons[sub1] + introns[sub1])
	print file
	"""now add last column, len 13 with a c composition
	c13total = counts[9][13] #how many reads were len 13 with a C at end, before removing genic overlaps
	c13three = float(c13total - counts[4][13]) / float(c13total) #what fraction of reads of len 13 with a C at end, overlapped with 3 prime regions
	c13five = float(c13total - counts[5][13]) / float(c13total)
	c13ex = float(c13total - counts[6][13]) / float(c13total)
	c13in = float(c13total - counts[7][13]) / float(c13total)
	c13remainder = float(1 - (c13three + c13five + c13ex + c13in))
	
	threeprime[21] = c13three
	fiveprime[21] = c13five
	exons[21] = c13ex
	introns[21] = c13in
	remainder[21] = c13remainder
"""

#now, we have 5 arrays that form the rows for a csv of this sample

	f = open(file[0:10] + '.csv', 'wt')
	writer = csv.writer(f)
	writer.writerow(threeprime)
	writer.writerow(fiveprime)
	writer.writerow(exons)
	writer.writerow(introns)
	writer.writerow(remainder)
	f.close()
