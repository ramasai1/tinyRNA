import os

for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/unique/"):
	print 'mkdir /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/CompositionStats2/' +  file[0:10] + '/'
