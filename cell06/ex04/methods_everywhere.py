import sys
def shrink(s: str) -> str:
  print(s[:8])
    
def enlarge(s: str) -> str:
  if len(s) < 8:
    print(s +"Z"*(8-len(s)))
  else : 
    print(s)
    
if sys.argv == 1 :
  print("none")
else :
  for arg in sys.argv[1:]:
        if len(arg) > 8:
          shrink(arg)
        elif len(arg) < 8:
          enlarge(arg)
        else:
          print(arg)
    
