import sys
input = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCACCAGATCATCTCGTATGCC"
count = 0
for line in sys.stdin:
	if input in line:
		count = count + 1

print "found: " + str(count) 
