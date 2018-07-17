#定义x，binary,do_not,y 变量值
x = "There are %d type of pepple." % 10
binary ='binary'
do_not = "don't"
y = "Those who knows %s and those who %s." % (binary,do_not)

print x
print y

print "I said: %r." % x
print "I said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e