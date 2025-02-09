'''

Create your own MyEnumerate class, such that someone can use it instead of enumerate.
It will need to return a tuple with each iteration, with the first element in the tuple being the index (starting with 0)
and the second element being the current element from the underlying data structure.
Trying to use MyEnumerate with a noniterable argument will result in an error.
'''

class MyEnumerate():
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        current_index = self.index
        current_data = self.data[current_index]
        self.index += 1
        return (current_index, current_data)


e = MyEnumerate('abcdef')

#print(e.__next__())
for i, j in e:
    print(i)

