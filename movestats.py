import os
import sys
for line in sys.stdin:

	for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/CompositionStats/"):
		
		if file[0:10] == line[0:10] and "csv" in file:

			print 'mv /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/CompositionStats/' + file + ' /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/CompositionStats2/' + line[0:10] + '/' + file
