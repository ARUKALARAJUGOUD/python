import math
class Calculator:
  def __init__(self,n):
    self.n = n
  def get_square(self):
    return self.n ** 2
  def get_cube(self):
    return self.n ** 3
  def get_square_root(self):
    return math.sqrt(self.n)

c1 =  Calculator(5)   
print(f"square = {c1.get_square()}") 
print(f"square = {c1.get_cube()}") 
print(f"square = {round(c1.get_square_root() , 3)}") 