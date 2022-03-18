def ispriem(x):
   if x > 1:
       for n in range(2,int(x/2)+1):
           if x%n == 0:
               return False
       return True
   else:
      return False