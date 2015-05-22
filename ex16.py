
from sys import argv

script, filename = argv


target = open(filename, 'r')
file_contents = target.read()
target.close()
print "The file contains:"  
print file_contents

print "We're going to erase %r." % filename
print "If you don't want that, hit Ctrl-C (^C)"
print "If that is okay, hit RETURN."

raw_input("?")

target = open(filename, 'w')
print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, I'll close it."
target.close()


