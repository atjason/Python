
try:
	file = open("aaa.txt")

except IOError as e:
	print "IOError: [Errno %d] %s" % (e.errno, e.strerror)

except (SystemError, TypeError):
	print "Catch multiple errors at a time."

except:
	print "All uncatched errors come here."

else:
	print "Come here if no error occurs"
	file.close()

finally:
	print "Always come here no matter has error or not."

###
print "\n", "#" * 10

class MyError(Exception):

	def __init__(self, description):
		self.description = description

	def __str__(self):
		return repr(self.description)

try:
	raise MyError("Test error.")

except MyError as error:
	print error.description
	print error # It's also fine as defined MyError:__str__

###

import traceback

print '########################################################'
print "1/0 Exception Info"
print '---------------------------------------------------------'
try:
    1/0
except Exception, e:
    print 'str(Exception):\t', str(Exception)
    print 'str(e):\t\t', str(e)
    print 'repr(e):\t', repr(e)
    print 'e.message:\t', e.message
    print 'traceback.print_exc():'; traceback.print_exc()
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
print '########################################################'
print '\n########################################################'  
print "i = int('a') Exception Info"
print '---------------------------------------------------------'
try:
    i = int('a')
except Exception, e:
    print 'str(Exception):\t', str(Exception)
    print 'str(e):\t\t', str(e)
    print 'repr(e):\t', repr(e)
    print 'e.message:\t', e.message
    print 'traceback.print_exc():'; traceback.print_exc()
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
print '########################################################'

