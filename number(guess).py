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
        
# Guessing game with oop 2/3/23
# 1.Create a guessing game class and they have three methode 
    #- Init ,
    #-Play method for user input the number and it's have try-except for value erro
    #- play again (loop)
import random
class GuessingGame:
    def __init__(self):
        self.random_number = random.randint(1, 10)
        self.win = False
        self.turns = 0
    
    def play(self):
        while self.win == False:
            try:
                guess = int(input("Enter a number between 1 and 10: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            
            self.turns += 1
            
            if guess == self.random_number:
                print("You won!")
                print(f"Number of turns you have used: {self.turns}")
                self.win = True
                break
            else:
                if self.random_number > guess:
                    print("The number as low. Please enter a higher number.")
                else:
                    print("the number was high. Please enter a lower number.")
    
    def play_again(self):
        self.random_number = random.randint(1, 10)
        self.win = False
        self.turns = 0
        self.play()
game = GuessingGame()
game.play()
game.play_again()
