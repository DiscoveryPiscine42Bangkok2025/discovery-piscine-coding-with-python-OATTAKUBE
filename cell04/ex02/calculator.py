a = int(input("Give me the first number: "))
b = int(input("Give me the second number: "))
print("Thank you!")
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
if(b ==0): 
  print("Error cannot be divided by 0")
else :
  print(f"{a} / {b} = {int(a/b)}")
print(f"{a} * {b} = {a*b}")