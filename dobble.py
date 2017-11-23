#!/usr/bin/env python3
""" Dobble game
    Usage: 
        python3 dobble.py
"""

from urllib.request import urlopen
from random import sample, choice, randint

def fetch_words(url):
    """ Fetch list of words from URL
    Args:
        url: The URL of a UTF-8 text doc.
    Returns:
        A list of strings containing the words
    """
    with urlopen(url) as content:
        words = []
        for line in content:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                words.append(word)
    return words

  
def create_sets(my_set):
    """ Create two unique sets
    Args:
        my_set - initial set to divide
    Returns:
        Two unique sets with one common element      
    """ 
    ful_set = sample(dob_set,15)
    set1 = ful_set[:8]
    set2 = ful_set[8:]
    matcher = choice(set1)
    ##print(matcher)
    place = randint(0,len(set2))
    set2.insert(place,matcher)
    return set1, set2

def main():
	url = 'http://sixty-north.com/c/t.txt'
	dob_set = set(fetch_words(url))
	


if __name__ == '__main__':
	main()













