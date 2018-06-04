a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
if ( a in list ):
	print "Line 1 - a is available in the given list"
else:
	print "Line 1 - a is not available in the given list"
if ( b not in list ):
	print "Line 2 - b is not available in the given list"
else:
	print "Line 2 - b is available in the given list"
a = 2
if ( a in list ):
	print "Line 3 - a is available in the given list"
else:
	print "Line 3 - a is not available in the given list"