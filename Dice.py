#Dice
import time as t
a=t.time_ns()
print(a)
while (a%10==0 or a%10==7 or a%10==8 or a%10==9 ):
  a=t.time_ns()
  print(a)
print(a%10)