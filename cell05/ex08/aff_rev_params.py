import sys
num = len(sys.argv) -1
if num < 2:
  print("none")
else : 
   for param in sys.argv[:0:-1]:
        print(param)