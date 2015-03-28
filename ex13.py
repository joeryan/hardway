# exercise on unpacking variables and argv

from sys import argv

print "The script name is: ", argv[0]
for inputs in argv[1:]:
    print "You sent in: ", inputs

