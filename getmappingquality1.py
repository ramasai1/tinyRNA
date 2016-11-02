import sys

for file in sys.stdin:
	print 'cat /cbcb/project-scratch/tinyRNAproj/mapqual/' + file[0:10] + '.txt' + ' | sort -n | uniq -c > /cbcb/project-scratch/tinyRNAproj/mapqualdist/' + file[0:10] + '.txt'
