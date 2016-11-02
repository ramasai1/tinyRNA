import os

for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/mappedreads/bamfiles/"):
	print 'bedtools bamtobed -i /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/mappedreads/bamfiles/' + file + ' > /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/mappedreads/bedfiles/' + file[0:10] + '.bed'
