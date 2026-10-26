class Employee:
  name = "Default Name"
  age = 22
  salary = 120000
  @staticmethod
  def Static_Method():
    print("this is static method")

  def __init__(self,name,age,salary):
    self.name = name
    self.age = age
    self.salary = salary
  def Info(o):  
    print(f"Employee name = {o.name} , salary = {o.salary} and age is {o.age}")

  def Greet(self):
    print("good after noon")

employee1 = Employee("Arukala Raju", 22 , 150000)
print(f"Name = {employee1.name}")
employee1.Greet()
Employee.Info(employee1)
Employee.Static_Method()
employee1.Static_Method()
