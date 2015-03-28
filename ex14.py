from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you some questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What operating system do you use?"
computer = raw_input(prompt)

print '''
alright, so you said %r about liking me.
You live in %r.  Not suure where that is.
And you use the %r operating system. Nice.
''' % (likes, lives, computer)
