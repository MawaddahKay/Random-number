"""
Program: random.com
Author: Mawaddah
Last date modified:21/11/22
"""
# guess the number game in Python
import random
random_number = random.randint(1,10)
win = False
Turns =0
while win==False:
    Your_guess = input("Enter a number between 1 and 10")
    Turns +=1
    if random_number==int(Your_guess):
        print("You won!")
        print("Number of turns you have used: ",Turns)
        win == True
        break
    else:
     if random_number>int(Your_guess):
        print("was low, Please enter a higher number")
     else:
        print("was high, please enter a lower number")
