'''
Write a function, strsort, that takes a single string as its input and returns a string.
The returned string should contain the same characters as the input, except that its characters
should be sorted in order, from the lowest Unicode value to the highest Unicode value.
For example, the result of invoking strsort('cba') will be the string abc.
'''

def strsort(word):
    return ''.join(sorted(word))

if __name__ == "__main__":
    print(strsort('cba'))