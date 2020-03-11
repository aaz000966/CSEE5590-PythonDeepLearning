# TODO
# Author: Team 8
# Usecase: concatenating two dictionaries
import operator
from collections import Counter


def main():
    dict1 = {
        'Randomness': 5,
        'Makes': 7,
        'Life': 8,
        'Better': 8,
        'Though!': 2
    }
    dict2 = {
        'Better': 8,
        "Call": 20,
        'Soul': 7,
        'Though!': 1
    }
    # This way, The value of these words will be increased,we thought
    #  this is a better way to represent the result of this method
    myDict = ToConc(dict1, dict2)
    print(myDict)


def ToConc(dict1, dict2):
    # Converting the two to a Counter type
    d1 = Counter(dict1)
    d2 = Counter(dict2)
    toReturn = d1 + d2

    # Calling dict() since the output of this method is in counter type (subclass of dictionary)
    return dict(sorted(toReturn.items(), key=operator.itemgetter(1), reverse=True))


if __name__ == '__main__':
    main()
