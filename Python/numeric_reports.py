'''
Guess the number

Problem Statement: 
Write a function (run_timing) that asks how long it took for you to run 10 km. 
The function continues to ask how long (in minutes) it took for additional runs, until the user presses Enter. 
At that point, the function exits--but only after calculating and displaying the average time that the 10 km runs took.

'''


def run_timing():
    runs = []   

    while(True):
        try:
            user_input = float(input('Enter 10 Km run time: '))
            runs.append(user_input)
            user_input = 0
        except ValueError as e:
            print(f'This is not a valid number{user_input}.')
            if user_input == 0:
                break           

    list_len = len(runs)
    avg = sum(runs)/list_len

    return f'Average of {avg}, over {list_len} runs'





if __name__ == '__main__':
    print(run_timing())


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