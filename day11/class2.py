class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("David", 2000)
"This would create second object of Employee class"
emp2 = Employee("John", 5000)
emp3= Employee("Abc",7000)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print "Total Employee %d" % Employee.empCount