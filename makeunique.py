import os
for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/unique/"):
	if "combsort" in file:
		print 'python /cbcb/project-scratch/tinyRNAproj/scripts/getUniqueCombined.py < /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/unique/' + file + ' > /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/unique/' + 'final_' + file 
