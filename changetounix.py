import os

for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/uniqueEndCbed/"):
	print 'sed ' + """'s/  */""" + """\\t/g' """ +  '/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/uniqueEndCbed/' + file  + ' > /cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/uniqueEndCBed/' + file
