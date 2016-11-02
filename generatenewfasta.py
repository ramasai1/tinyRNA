import os
for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/15addedBedNonLength/"):
	print 'bedtools getfasta -s -fi /cbcb/project-scratch/tinyRNAproj/DEMO/bowtie/chrFASTAfiles/hg19chr.fa -bed /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/15addedBedNonLength/' + file + ' -fo /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/15addedFastaNonLength/' + file[0:10] + ".fa"
