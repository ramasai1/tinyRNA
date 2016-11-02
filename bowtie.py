import os

for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/finalClipped/"):
	print 'bowtie2 -a -q -x /cbcb/project-scratch/tinyRNAproj/DEMO/bowtie/hg19refdemo/hg19 -U /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/finalClipped/' + file + ' -S /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/mappedreads2/samfiles/' + file[0:10] + '.sam'
