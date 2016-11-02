import os

for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/mappedreads/bedfiles/"):
	print "/cbcb/project-scratch/tinyRNAproj/software/bedtools-2.17.0/bin/subtractBed -a /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/mappedreads/bedfiles/" + file + " -b /cbcb/project-scratch/tinyRNAproj/DEMO/bowtie/miRNArefdemo/mirna_hsa.bed -A > /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/mappedreads/mirnaremovedbed/" + file
