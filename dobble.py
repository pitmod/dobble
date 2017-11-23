#!/usr/bin/env python3
""" Dobble game
    Usage: 
        python3 dobble.py
"""

import time
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
    ful_set = sample(my_set,15)
    first_set = ful_set[:8]
    second_set = ful_set[8:]
    matcher = choice(first_set)
    ##print(matcher)
    place = randint(0,len(second_set))
    second_set.insert(place,matcher)
    return list(first_set), list(second_set)




def main():
    url = 'http://sixty-north.com/c/t.txt'
    dob_set = set(fetch_words(url))
    reps = 3
    times = []
    for i in range(reps):
        set1, set2 = create_sets(dob_set)
        print(set1)
        print()
        print(set2) 
        print()
        while True:
            start_time = time.time()
            times.append(start_time)
            ind1 = int(input("Enter index1: "))
            ind2 = int(input("Enter index2: "))
            if set1[ind1] == set2[ind2]:
               break
        print("Correct. Your score: --- %s seconds ---" % (time.time() - start_time))	
        print()
    print()
    print(times)
    print("Best time is: ",min(times) )

if __name__ == '__main__':
	main()

