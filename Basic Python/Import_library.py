#Learn hoe to import library.
 import math # importing math library.
 print(math.factorial(4))#using math opration.


# make a coin flip program using random library.
 import random
 a = random.random()# generating a random number between 0 and 1.
 if (a < 0.5): # using if condition to check the random number.
     print("Heads")
 else:
     print("Tails")


#Lets simulates a dice (six faces).
 import random
 print(random.randrange(1,7)) # generating a random number between 1 and 6.


 
# Lets simulate two dice.
 import random
 dice1 = random.randrange(1,7)
 print(dice1)
 dice2 = random.randrange(1,7)
 print(dice2)
 total = dice1 + dice2
 print ("Sum of two dicesis :", total)


# Lets try calender library.
 import calendar
 print(calendar.month(2000,2))
 print(calendar.calendar(2025))


 from calendar import *
 print(month(2025,6))


from random import *
print(randrange(1,7))
