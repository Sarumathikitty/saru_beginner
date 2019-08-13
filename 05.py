number = int(input(" "))
sum = 0
temp = number
while temp > 0:
   dig = temp % 10
   sum += dig ** 3
   temp //= 10

if number == sum:
   print(number,"is an Armstrong number")
else:
   print(number,"is not an Armstrong number")
