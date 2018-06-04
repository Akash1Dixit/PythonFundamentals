# Python code to illustrate append() mode
file = open('write.txt','a')
a=raw_input("Enter the additional contents you want to add")
file.write(a)
file.close()