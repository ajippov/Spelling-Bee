# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 20:17:42 2022

@author: ajipp

Spelling Bee Solver

After suffering for a while trying to use pandas, I decided to cave and look online for alternatives.

As a side note, the dictionary I use plays it pretty loose with the definition of a word. Hopefully, you're able to
source a better one than I.
    
"""

import pandas as pd

dictionary = open("Downloads\Dictionary.txt")
rawDict = dictionary.read()
words = rawDict.split()

words = [word for word in words if word.isalpha() and len(word) >= 4]
for i in range(len(words)):
    words[i] = words[i].lower()
    
def solver(letters, yellowLetter):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']
    
    solutionSet = []
    badLetters = [l for l in alphabet if l not in letters]
    
    for w in words:
        if yellowLetter in w:
            if w not in solutionSet:
                if any(l in badLetters for l in w) == False:
                        solutionSet.append(w)
    
    return solutionSet

def calcPoints(letters, sset):
    
    points = []
    
    for w in sset:
        if len(w) == 4:
            points.append(1)
        elif len(w) > 4 and len(w)< 7:
            points.append(len(w))
        elif len(w) >= 7:
            points.append(len(w)) not in [c in w for c in letters]
        else:
            points.append(len(w) + 7)
            
    return points
                
solver(['o', 'p', 'w', 'l', 'r', 'h', 'i'], 'o')
calcPoints(['o', 'p', 'w', 'l', 'r', 'h', 'i'], solver(['o', 'p', 'w', 'l', 'r', 'h', 'i'], 'o'))


def main():
    usr = input("PLease type the set of letters: ")
    yellow = input("Please type the center letter: ")
    letters = usr.split(" ")
    
    info = pd.DataFrame(columns=["Word", "Points"])
    
    m = solver(letters, yellow)
    n = calcPoints(letters, m)
    
    print(m)
    print(n)
    
    info = list(zip(m, n))

    return info

if __name__ == '__main__':
    main()
    