import os
string = "TGGAATTCTCGGGTGCCAAGG"
adaptcount = 0
linecount = 0
filelist = []
for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/Ntest"):
	filelist.append(file)

for i in range (0, len(filelist)):
	print "file: " + filelist[i],
	with open("/cbcb/project-scratch/tinyRNAproj/samples/Ntest/" + filelist[i], "rb+") as fo:
		linecount = 0
		adaptcount = 0
		for line in fo:
			if line[0:4] == "@SRR":
				linecount = linecount + 1
			if line[0:21] == string:
				adaptcount = adaptcount + 1
		print "reads starting with adapter: " + str(adaptcount),
		print "total reads: " + str(linecount)		
	
