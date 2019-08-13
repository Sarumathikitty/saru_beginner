c = 360
d = 380
 
for number in range(c,d + 1):
   sum = 0
   temp = n
   while temp > 0:
       dig = temp % 10
       sum += dig ** 3
       temp //= 10
 
   if n == sum:
       print(n)
