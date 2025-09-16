#!/usr/bin/env python3
i = 0
while i  < 11 :
  print(f"Table de {i}:", end=" ")
  j = 0
  while j < 13:
    print(i*j , end=" ")
    j+=1
  print()
  i+=1