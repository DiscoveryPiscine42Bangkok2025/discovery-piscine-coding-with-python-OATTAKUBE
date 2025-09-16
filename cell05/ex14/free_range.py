import sys
if len(sys.argv) == 3 :
  start = int(sys.argv[1])
  stop = int(sys.argv[2])
  arr = list(range(start,stop+1))
  print(arr)
else:
  print("none")