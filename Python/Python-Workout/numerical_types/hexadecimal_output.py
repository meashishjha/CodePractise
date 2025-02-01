'''
you need to write a function (hex_output) that takes a hex number and returns the decimal equivalent.
That is, if the user enters 50, you’ll assume that it’s a hex number (equal to 0x50) and will print
the value 80 to the screen. And no, you shouldn’t convert the number all at once using the int function,
although it’s permissible to use int one digit at a time.
function to convert hexadecimal to  integer
'''

def hex_output(number):
    total_int = 0
    for position, value in enumerate(reversed(number)):
        total_int += int(value,16) * (16**position)

    return total_int


if __name__ == "__main__":
    print(hex_output('50'))