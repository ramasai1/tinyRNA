import os
for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FASTQ"):
	print "python /cbcb/project-scratch/tinyRNAproj/scripts/findN.py < /cbcb/project-scratch/tinyRNAproj/samples/FASTQ/" + file + " > /cbcb/project-scratch/tinyRNAproj/samples/Ntest/" + file[0:-5] + "fastq" 
