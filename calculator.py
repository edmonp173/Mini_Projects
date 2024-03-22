num = int(input("give num: "))
if 1500 <= num <= 2700:
 if num %7 == 0:
  if num %5 == 0:
   print(num)
  else:
   print("not 7")

 else:print("not 5")


else:
 print("no")