import sys
import re
if len(sys.argv) != 2 :
  print("none")
else :
  word = sys.argv[1]
  matches = re.findall("z",word)
  
  if matches :
    print("z"*len(matches))
  else :
    print("none")