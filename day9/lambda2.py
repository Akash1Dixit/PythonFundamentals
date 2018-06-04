#lambda returns a function
#assigning name to function returned is optonal

print (lambda x,y,z: x+y+z)(2,3,4)

#here we are assigning name to the function returned

f = lambda x,y,z: x+y+z

#calling the function and storing the result
result = f(2,3,4)
print result

#same task using def statement
def g():
    def f(x,y,z):
        return x+y+z
    return f
f = g()
result = f(2,3,4)
print result
