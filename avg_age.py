class Employee:
  def __init__(self,fname,lname,age):
    self.fname = fname
    self.lname = lname
    self.age = age


employees = [Employee('name1','name2',22),
Employee('name1','name2',30),
Employee('name1','name2',32),
Employee('name1','name2',20),
Employee('name1','name2',23)]

ages = [Emp.age for Emp in employees]
print('Average age of the employees : {}'.format(sum(ages)/len(ages)))
