import os
for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/Bowtie2/bedfiles/"):
	print 'bedtools getfasta -s -fi /cbcb/project-scratch/tinyRNAproj/DEMO/bowtie/chrFASTAfiles/hg19chr.fa -bed /cbcb/project-scratch/tinyRNAproj/Bowtie2/bedfiles/' + file + ' -fo /cbcb/project-scratch/tinyRNAproj/samples/lengthcsv/aftermaptogenome/' + file
