#lists operations

L =[ 123, 'welcome' , 456, 'hello']
#indexing
print L[0]

#slicing
print L[:-1]

#concatenation
L=L + [ 1,2,3]
print L

print L*2

#delete from list
#remove: removes the first matching value, not a specific index
#del: removes a specific index
#pop: returns the removed element
L.remove('hello')
print L

del L[0]

print L
print L.pop(1)

#mutable
L.append(1)
print(L)

#change lists in place
L[0]=8
print L
#s = 'python'
#s[0]='z'
#"""
#s='Python'
#s.append('World')
#strings are not mutable
#"""
L.extend(['hi','world'])
print(L)

#insert 4 at position 2
L.insert(2,4)
print(L)

#sort the list
L.sort()
print'Sorted list: ',L

#reverse the list
L.reverse()
print 'Reversed list: ',L

#bound checking
#print L[100]

#nesting
l = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print 'Nested list:'
print l