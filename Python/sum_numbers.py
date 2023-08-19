'''
Guess the number

Problem Statement: 
The challenge here is to write a mysum function that does the same thing as the built-in sum function. 
However, instead of taking a single sequence as a parameter, it should take a variable number of arguments. 
Thus, although you might invoke sum([1,2,3]), you’d instead invoke mysum(1,2,3) or mysum(10,20,30,40,50).

'''


def mysum(*args):
    totalsum = 0
    for i in args:
        totalsum += i

    return totalsum

   




if __name__ == '__main__':
    print(mysum(10,20,3,4,5))
    print(sum([1,2,3],6))


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