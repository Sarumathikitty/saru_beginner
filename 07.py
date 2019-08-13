number = 7
fac = 1
if number < 0:
   print("Sorry, fact does not exist for negative numbers")
elif number == 0:
   print("The fact of 0 is 1")
else:
   for i in range(1,number + 1):
       fact = fact*i
   print("The fact of",num,"is",fact)
