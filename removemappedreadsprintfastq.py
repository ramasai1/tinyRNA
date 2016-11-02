import sys
fileid = ""
idlist = []
for line in sys.stdin: 
	fileid = line[0:10]
	idlist.append(line.strip())
f = open("/cbcb/project-scratch/tinyRNAproj/samples/finalClipped/" + fileid + "_1out.fastq", 'r+')
linelist = f.readlines()
line = ""
linecount = 1
for i in range(0, len(linelist)):
	line = linelist[i]
	
	if linecount == 1:
		line1 = line
	elif linecount == 2:
		line2 = line
	elif linecount == 3:
		line3 = line
	elif linecount ==4:
		line4 = line
		linecount = 0
		headlist = line1.split()
		header = headlist[0]
		if header[1:] not in idlist and len(line2) == 10:
			print line1,
			print line2,
			print line3,
			print line4,
	linecount = linecount + 1
f.close()


