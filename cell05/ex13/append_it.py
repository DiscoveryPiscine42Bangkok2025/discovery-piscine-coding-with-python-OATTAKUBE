import sys
import re

if len(sys.argv) == 1:
    print("none")
else:
    for word in sys.argv[1:]:
        if re.search(r"ism$", word):   
            continue                 
        else:
            print(word + "ism")
