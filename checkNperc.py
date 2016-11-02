import os
string = '"percent"'
for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/Ntest"):
	print "grep -e " + string + " /cbcb/project-scratch/tinyRNAproj/samples/Ntest/" + file
	print "ls /cbcb/project-scratch/tinyRNAproj/samples/Ntest/" + file
