import sys
linecount = 1
tmp = ""
for line in sys.stdin:
	sample = line.strip()
	fileid = open('/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/unique/' + sample, "r")
	newfile = open(sample[0:10] + '.bed', "w")
	for tline in fileid.readlines():
		if linecount == 1:
			chrom = tline.find(':')
			intv = tline.find('-')
			strand = tline.find('(')
			if float(tline[chrom + 1:intv]) >= 15.0:
				newfile.write(tline[1:chrom] + "\t" + str(int(tline[chrom + 1:intv]) - 15) + "\t" + str(int(tline[intv + 1: strand]) + 15) + "\t" + sample[0:10] + "\t1\t" + tline[strand + 1] + "\n")
			linecount = 2	
		elif linecount == 2:
			linecount = 1
	newfile.close()
	fileid.close()


