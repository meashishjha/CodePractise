'''
Write a function, most_repeating_word, that takes a sequence of strings as input. The function should return the string that contains the greatest number of repeated letters. In other words

For each word, find the letter that appears the most times.

Find the word whose most-repeated letter appears more than any other.

That is, if words is set to

words = ['this', 'is', 'an', 'elementary', 'test', 'example']
then your function should return elementary. That’s because

this has no repeating letters.

is has no repeating letters.

an has no repeating letters.

elementary has one repeating letter, e, which appears three times.

test has one repeating letter, t, which appears twice.

example has one repeating letter, e, which appears twice.

So the most common letter in elementary appears more often than the most common letters in any of the other words.
(If it’s a tie, then any of the appropriate words can be returned.)
'''
from collections import Counter

def most_repeating_word(words):
    return max(words, key=lambda x: Counter(x).most_common(1)[0][1])



if __name__ == "__main__":
    string_list = ['this', 'is', 'an', 'elementary', 'test', 'example']
    print(most_repeating_word(string_list))