'''
Number Guessing Game
Write a function (guessing_game) that takes no arguments.
When run, the function chooses a random integer between 0 and 100 (inclusive).
Then ask the user to guess what number has been chosen.
Each time the user enters a guess, the program indicates one of the following:
Too high
Too low
Just right
If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
The program only exits after the user guesses correctly.
'''
import random

def guessing_game():
    number = random.randint(0, 100)

    while True:
        input_number = int(input("Enter your guess number from 0-100\n"))
        if input_number == number:
            print(f"you guessed it right! The number is {number}")
            break
        elif input_number >= 0 and input_number < (number - 5):
            print("too less, try again please!")
        elif input_number >= (number - 5) and input_number <= (number + 5):
            print("Almost in the range!")
        elif input_number > (number+5) and input_number <=100:
            print("too high, try again!")



if __name__ == "__main__":
    guessing_game()