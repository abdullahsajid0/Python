#this program alllows user to guess a number
import random
number = random.randint(1, 100)
guess = None    
while guess != number:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number.")
    except ValueError:
        print("Invalid input! Please enter a valid number.") 
