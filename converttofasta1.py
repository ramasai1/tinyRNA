import os

for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/genicregionremovedbednonc/upstream/"):
	print 'bedtools getfasta -s -fi /cbcb/project-scratch/tinyRNAproj/DEMO/bowtie/chrFASTAfiles/hg19chr.fa -bed /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/genicregionremovedbednonc/upstream/' +  file + ' -fo /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/genicregionremovedfastanonc/upstream/' + file[0:10] + '.fa'
