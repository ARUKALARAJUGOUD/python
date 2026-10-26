# def generate_table(n):
#   table = ""
#   for i in range(1,11):
#     table += f"{n} x {i} = {n * i} \n"

#   with open(f"tables/table_{n}.txt","w") as f:
#     f.write(table) 
#   print(table) 

# for i in range(1,21):
#   generate_table(i)

with open("file.txt","r") as f:
  data = f.readline().lower()
  print("data from the file " , data)
  if ("donkey" in data ):
   new_data =  data.replace("donkey","#")
   with open("file.txt","w") as file:
     file.write(new_data)

   print(new_data)  
  # print(f.readline().lower())