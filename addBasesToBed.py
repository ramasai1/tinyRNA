import os
from os.path import join as pjoin

for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/bylengths/bedfiles/"):
	for filename in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/bylengths/bedfiles/" + file + "/"):
		sample = filename.strip()
		fileid = open('/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/bylengths/bedfiles/' + file + '/' + filename, "r")
		path_to_file = pjoin("/cbcb", "project-scratch", "tinyRNAproj", "samples", "FINALSAMPLES", "15addedbedfiles", file, filename)
		newfile = open(path_to_file, "w")
		for line in fileid.readlines():
			tline = line.strip()
			chrom = tline.find('\t', 0, len(tline))
			intv = tline.find('\t', chrom + 1, len(tline))
			intv2 = tline.find('\t', intv + 1, len(tline))
			rest = tline[intv2 : len(tline)]
			print file + '/' + filename
			if int(tline[chrom + 1:intv]) >= 15:
				newfile.write(tline[0:chrom] + "\t" + str(int(tline[chrom + 1:intv]) - 15) + "\t" + str(int(tline[intv + 1: intv2]) + 15) + "\t" + rest + "\n")
		newfile.close()
		fileid.close()
