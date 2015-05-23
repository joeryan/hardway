def print_two(*args):
	arg1, arg2 = args
	print "arg1 = %r, arg2: %r" % (arg1, arg2)

# *args is a bit pointless, we could just do this
def print_two_again(arg1, arg2):
	print "arg1 = %r, arg2: %r" % (arg1, arg2)

# this takes just one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothing"

print_two("Joe", "Momma")
print_two_again("Smokin", "Joe")
print_one("First!")
print_none()
