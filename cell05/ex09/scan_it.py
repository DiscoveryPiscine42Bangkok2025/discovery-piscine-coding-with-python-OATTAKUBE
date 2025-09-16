import sys
import re
if len(sys.argv) != 3 :
  print("none")
else :
  key_word = sys.argv[1]
  word = sys.argv[2]
  
  matches = re.findall(key_word,word)
  if matches :
    print(len(matches))
  else :
    print("none")