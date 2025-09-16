import sys
if len(sys.argv) != 2:
  print("none")
else : 
  word = input("What was the parameter? ")
  if(sys.argv[1] == word):
    print("Good Job!")
  else :
    print("Nope, sorry...")