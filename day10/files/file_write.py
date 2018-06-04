# Python code to create a file
file = open('write.txt','w')
a=raw_input("Enter Contents")
file.write(a)
file.write("\n The above lines are the user input")
file.close()