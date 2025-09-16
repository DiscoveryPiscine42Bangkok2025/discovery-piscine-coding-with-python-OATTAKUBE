str_num= str(input("Give me a number: "))
float_num = float(str_num)
if float_num.is_integer():
  print("This number is an integer.")
else:
  print("This number is an decimal.")