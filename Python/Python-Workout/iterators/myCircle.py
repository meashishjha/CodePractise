'''
Define a class, Circle, that takes two arguments when defined: a sequence and a number.
The idea is that the object will then return elements the defined number of times.
If the number is greater than the number of elements, then the sequence repeats as necessary.
You should define the class such that it uses a helper (which I call CircleIterator).
'''

class CircleIterator():
    def __init__(self, data, length):
        self.data = data
        self.length = length
        self.index = 0

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        data_length = len(self.data)
        value = self.data[self.index % data_length]
        self.index += 1
        return value

class Circle():
    def __init__(self, data, length):
        self.data = data
        self.length = length


    def __iter__(self):
        return CircleIterator(self.data, self.length)


c = Circle('abc', 5)
print(list(c))