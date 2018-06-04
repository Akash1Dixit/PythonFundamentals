#different ways of creating a dictionary

#first
#dictionaries are not ordered
D={'name':'abc' , 'l_name':'xyz' , 'age':22}
print D

#second
d={}
d['name']='abc'
d['l_name']='xyz'
d['age']=22
print(d)

#third
H=dict(name='abc', l_name='xyz', age=22)
print(H)

print '-'*25
#length of Dictionary
print 'length of dictionary: ',len(H)

#print  specific value
print(d['name'])

#adding 1 to age
d['age'] = d['age'] + 1
print d

#mutable
d['name']='def'
print d

#deletion
del d['name']
print d

print d.pop('l_name')
print d

print '-'*25
#nesting
record={'name':{'first':'Bob','lname':'Willaim'},
        'jobs':['manager','engineer'],
        'age':45}
print record
print record['name']['first']
print record['jobs'][0]

print '-'*25


print '-'*25
#methods of dictionary
print D.keys()
print D.values()
print D.items()
print D.get('name')
