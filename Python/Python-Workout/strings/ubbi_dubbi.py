'''
Write a function (called ubbi_dubbi) that takes a single word (string) as an argument.
It returns a string, the word’s translation into Ubbi Dubbi. So if the function is called with octopus,
the function will return the string uboctubopubus. And if the user passes the argument elephant, you’ll output ubelubephubant.
'''

def ubbi_dubbi(word):
    output = []
    for char in word:
        if char in 'aeiou':
            output.append(f"ub{char}")
        else:
            output.append(char)

    return ''.join(output)

if __name__ == "__main__":
    print(ubbi_dubbi('elephant'))