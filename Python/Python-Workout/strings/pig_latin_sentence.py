'''
write a Python function (pig_latin) that takes a string as input, assumed to be an English word.
The function should return the translation of this word into Pig Latin. You may assume that the
word contains no capital letters or punctuation.
'''
def pig_latin(word):
    if word[0].lower() in 'aeiou':
        output = f'{word}way'
    else:
        output = f'{word[1:]}{word[0]}way'
    return output

def pig_latin_sentence(sentence):
    output = []
    for word in sentence.split():
        output.append(pig_latin(word))
    return ' '. join(output)

if __name__ == "__main__":
    print(pig_latin_sentence('this is a test translation'))

