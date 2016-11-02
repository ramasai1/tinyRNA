import os
dirname = "/cbcb/project-scratch/tinyRNAproj/"

for file in os.listdir(dirname + "Bowtie2/mirnaremovedmappedsequences/"):
	print dirname + "software/bbmap/filterbyname.sh in=" + dirname + "samples/finalClipped/" + file[0:10] + "_1out.fastq " + "out=" + dirname + "samples/finalClippedmirnaRemoved/" + file[0:10] + ".fq" + " names=" + dirname + "Bowtie2/mirnaremovedmappedsequences/" + file
