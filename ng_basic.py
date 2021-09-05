# MY FIRST PROJECT
# NUMBER GUESSER

# library 
import random

# just to see if it works
class Number_Guesser:
      def ___init___(self, number):
          self.number = number

# variables
number = Number_Guesser(random.int(range(1, 1001)))
x = input()

# base structure
if x == number:
    print("You got it pal!")
elif x < number:
    print("More")
elif x > number:
    print("Less")
else:
    print("Only numbers allowed")
    

