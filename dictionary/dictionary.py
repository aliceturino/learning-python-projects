'''
This script asks you for a word and returns the meaning of that word by reading a json file and using the difflib module.
1 - Asks for the word.
2 - If spelling is correct: return the meaning of the word;
    If spelling is wrong: tries to choose another word that is in the dictionary and looks like the wrong spelling;
3 - If it finds the correct word: asks the user if it is what they meant;
    If it doesn't find the correct word: return that the word doesn't exist.
github.com/aliceturino
'''

import json
from difflib import get_close_matches
# difflib ->  "This module provides classes and functions for comparing sequences."

data = json.load(open("dictionary.json")) # 1. type(data) 2. <class 'dict'>


def translate(word):
    word = word.lower() # letter case insensitive program
    if word in data: # if spelling is correct
        return data[word]
# if the spelling is incorret, tries to fix it
    elif len(did_you_mean) > 0:
        yn = input("Did you mean %s instead? (Y if yes/N if no): " % get_close_matches(word, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list: #making the program more user friendly
    for item in output:
        print(item)
else:
    print(output)
