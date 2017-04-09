from collections import Counter
from itertools import izip, count
from StringIO import StringIO


def write_to_file(lst, f):
    """
    INPUT: list, open file object
    OUTPUT: None
    Write the list to the file with line numbers, starting at 1.
    INPUT: ["a", "b", "c"]
    FILE CONTENTS:
    1 a
    2 b
    3 c
    Hint: Use enumerate for cleaner code
    """
    for i,item in enumerate(lst):
        f.write("{} {}\n".format(i+1, item))



def merge_files(f1, f2, out):
    """
    INPUT: open file, open file, open file
    OUTPUT: None
    f1 and f2 are two files with the same number of lines. Merge the contents
    together, separated with a comma.
    INPUT FILES:
    cat
    dog
    mouse
    rabbit
    OUTPUT FILE:
    cat,mouse
    dog,rabbit
    Hint: Use izip
    """
    f1lines=f1.read().splitlines()
    f2lines=f2.readlines()
    f3=zip(f1lines, f2lines)
    outli=[','.join(list(x)) for x in f3]
    out.write(''.join(outli))

    #z=[x for x in f1.readline()]




def key_in_value(d):
    """
    INPUT: dict
    OUTPUT: list
    Return the keys from the dictionary where the key is a member in the
    associated value.
    example:
    INPUT: {"a": ["b", "c", "a"], "b": ["a", "c"], "c": ["c"]}
    OUTPUT: ["a", "c"]
    Hint: Use iteritems
    (Can be done on one line with a list comprehension)
    """

    return [k for k,v in d.iteritems() if k in v]


def most_common_letters(sentence):
    """
    INPUT: string
    OUTPUT: list of strings
    Given a sentence, give the most common letter for each word.
    You should lowercase the letters. If there's a tie, include any of them.
    example:
    INPUT: "Welcome to Zipfian Academy!"
    OUTPUT: 'e t i a'
    Hint: use Counter and the string join method
    (It is possible to do this in one line, but you might lose some
    readability)
    """

    return ' '.join([Counter(x).most_common()[0][0] for x in sentence.lower().split()])


def merge_dictionaries(d1, d2):
    """
    INPUT: dict (string => int), dict (string => int)
    OUTPUT: dict (string => int)
    example:
    INPUT: {"a": 2, "b": 5}, {"a": 7, "c":10}
    OUTPUT: {"a": 9, "b": 5, "c": 10}
    Create a new dictionary that contains all the key, value pairs from d1 and
    d2. If a key is in both dictionaries, sum the values.
    """

    pass

if __name__ == '__main__':

    f1 = StringIO("cat\ndog\npig\n")
    f2 = StringIO("rabbit\nhorse\nmouse\n")
    with open('test.txt','w') as out:
        merge_files(f1,f2,out)
