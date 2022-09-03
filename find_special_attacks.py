import os, fnmatch, sys

matches = []
found = False
folder = ""
results = 0
original_stdout = sys.stdout

with open('output.txt', 'w') as f:
	sys.stdout = f

	print("FOLDER\tSPECIAL_ATTACKS")

	for root, dirnames, filenames in os.walk('monster2'):
		for filename in fnmatch.filter(filenames, 'special_attack*.msa'):
			found = True
			folder = root
			results += 1

			matches.append(os.path.join(root, filename))

		if found:
			print("%s\t%d" % (folder, results))
			found = False
			folder = ""
			results = 0

	sys.stdout = original_stdout
