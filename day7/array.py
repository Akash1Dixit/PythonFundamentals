# Python code to demonstrate the working of 
# array(), append(), insert()
 
# importing "array" for array operations
import array
 
# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3]) 

# printing original array
print ("The new created array is : \n")
for i in range (0,3):
    print (arr[i])
    print "\t"

print ("\r")

# using append() to insert new value at end
arr.append(4);

# printing appended array
print ("The appended array is : \t")
for i in range (0, 4):
    print (arr[i])
    print "\t"
    
# using insert() to insert value at specific position
# inserts 5 at 2nd position
arr.insert(2, 5)

print("\r")

# printing array after insertion
print ("The array after insertion is : \t")
for i in range (0, 5):
    print (arr[i])