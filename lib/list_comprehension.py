#!/usr/bin/env python3

def return_evens(num_list):
    evens = [number for number in num_list if number % 2 == 0]
    print(evens)
    return evens

# should return [2, 4, 0, 8, 8]
return_evens([1, 2, 3, 4, 7, 0, 5, 8, 8])

def make_exclamation(sentence_list):
    exclamationed = [sentence + "!" for sentence in sentence_list]
    return exclamationed