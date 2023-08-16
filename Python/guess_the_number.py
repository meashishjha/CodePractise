'''
Guess the number

Problem Statement: 
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
    number = random.randint(1,101)
    user_input = int(input())
    pass


if __name__ == '__main__':
    guessing_game()


#**************************************************************************
#* (C) Copyright 2020-2023 by Ashish Jha and                              *
#* Outshine Labs. All Rights Reserved.                                    *
#*                                                                        *
#* DISCLAIMER: The authors and publisher of this book have used their     *
#* best efforts in preparing the book. These efforts include the          *
#* development, research, and testing of the theories and programs        *
#* to determine their effectiveness. The authors and publisher make       *
#* no warranty of any kind, expressed or implied, with regard to these    *
#* programs or to the documentation contained in these books. The authors *
#* and publisher shall not be liable in any event for incidental or       *
#* consequential damages in connection with, or arising out of, the       *
#* furnishing, performance, or use of these programs.                     *
#**************************************************************************