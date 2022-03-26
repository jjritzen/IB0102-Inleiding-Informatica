from ispriem import ispriem
x=int(input("Hoeveel priemgetallen: "))
i = 1
teller = 1

while teller <= x:
   if ispriem(i) == True:
      regel = str(teller) + "e priemgetal: " + str(i)
      print(regel) 
      teller += 1
      i += 1
   else:
      i += 1