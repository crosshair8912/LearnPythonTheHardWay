from sys import argv
from os.path import exists

script,from_file,to_file = argv

print ("Copying from %s file to %s file") % (from_file,to_file)

in_file = open(from_file).read()

print ("The input file is %d bytes long") % len(in_file)
print "Does the output file exists?%s" % exists(to_file)
print ("Ready, hit RETURN to continue, CTRL-C to abort.")

raw_input()

out_file = open(to_file,'w')
out_file.write(in_file)

print ("Alright, everything is done.")

out_file.close()