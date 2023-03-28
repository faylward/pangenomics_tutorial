import sys, re, os

inputdir = sys.argv[1]
ortho = open(os.path.join(inputdir, "Orthogroups.tsv"), "r")
singletons = open(os.path.join(inputdir, "Orthogroups_UnassignedGenes.tsv"), "r")
output = open(sys.argv[2], "w")

for i in ortho.readlines():
	output.write(i)

for i in singletons.readlines():
	if i.startswith("Orthogroup"):
		pass
	else:
		output.write(i)

