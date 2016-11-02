import os

for file in os.listdir("/cbcb/project-scratch/tinyrnaproj/mapqualdist/"):
	f = open("/cbcb/project-scratch/tinyrnaproj/mapqualdist/" + file, "r")
	count = []
	for line in f.readlines():
		

