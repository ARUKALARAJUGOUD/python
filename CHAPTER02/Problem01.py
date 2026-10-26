class Programmer:
  office_name = "Microsoft"
  # pin

  def __init__(self,name , salary , pin):
    self.name = name
    self.salary = salary
    self.pin = pin
    print("object is created ")
  def Info(self):
    print(f"Name = {self.name} , salary = {self.salary} and pin is {self.pin}")  
p1 = Programmer("Rahul" , 1230000, 35469)
# iam doing some work
p1.Info()