x = [1,2,3,4,5]
y = [1,2,3,4,5,6,7,8,9,10]

comb = len(x) + len(y)
if comb % 3 == 0 and comb % 5 == 0:
   print("fizzbuzz")
elif comb % 3 == 0:
       print("Fizz")
elif comb % 5 == 0:
       print("Buzz")