import os

for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/mappedreads/samfiles/"):
	print 'samtools view -S -b /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/mappedreads/samfiles/' + file + ' > /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/mappedreads/bamfiles/' + file[0:10] + '.bam'
