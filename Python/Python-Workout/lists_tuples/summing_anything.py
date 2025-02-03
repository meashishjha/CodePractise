'''
This challenge asks you to redefine the mysum function we defined in chapter 1,
such that it can take any number of arguments. The arguments must all be of the same
type and know how to respond to the + operator. (Thus, the function should work with
numbers, strings, lists, and tuples, but not with sets and dicts.)
'''

def mysum(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item

    return output


if __name__ == "__main__":
    print(mysum([1,2,4], [8,3,9]))
    print(mysum('abc','def'))
    print(mysum())