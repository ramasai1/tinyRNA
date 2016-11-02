import os

for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/lengthcsv/afteradaptertrim/"):
	print 'fastq_to_fasta -i /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/lengthcsv/afteradaptertrim/' + file + ' -o /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/lengthcsv/afteradaptertrim/fasta/' + file[0:10] + '.fa'
