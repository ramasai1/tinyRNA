import os

for file in os.listdir("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/bylengths/25/textfiles/"):
	if 'new' in file:
		print file
		f = open("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/bylengths/25/textfiles/" + file, 'r')	
		lines = f.readlines()
		newfile = open("/cbcb/project-scratch/tinyRNAproj/samples/FINALSAMPLES/bylengths/25/textfiles/" + file[0:10] + '.txt', 'wt')
		for line in lines:
			elements = line.split('\t')
			if '\n' not in elements[0]:
				newfile.write(elements[3] + '\n')
		newfile.close()
		f.close()
