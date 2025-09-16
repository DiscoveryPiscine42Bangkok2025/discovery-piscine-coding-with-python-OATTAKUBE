import sys
def downcase_it(s: str)-> str:
    return s.lower();
if len(sys.argv) == 1:
  print("none")
else :
  for i in sys.argv[1:] :
    print(downcase_it(i))
  