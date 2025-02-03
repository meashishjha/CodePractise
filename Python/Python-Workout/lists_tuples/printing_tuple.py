'''
printing tuples

'''
PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def printing_tuples(words):
    words = sorted(words, key=lambda x:(x[1], x[0]))
    output = []
    for word in words:
        output.append(f"{word[1]:10}{word[0]:10}{word[2]:10}")

    return '\n'.join(output)


if __name__ =="__main__":
    print(printing_tuples(PEOPLE))