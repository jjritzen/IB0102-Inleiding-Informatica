from ispriem import ispriem
x=int(input("Hoeveel priemgetallen: "))
getal = 1
teller = 1

while teller <= x:
   if ispriem(getal) == True:
      regel = str(teller) + "e priemgetal: " + str(getal)
      print(regel) 
      teller += 1
      getal += 1
   else:
      getal += 1