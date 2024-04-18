#!/usr/bin/env python3

def return_evens(num_list):
    divided_list = [num % 2 for num in num_list]
    even_list = [num for num in num_list if num % 2 == 0]
    if(divided_list.count(not 0) == len(divided_list)): return []
    else: return even_list

def make_exclamation(sentence_list):
    if(len(sentence_list) == 0): return []
    else: 
        sentence_list = [sentence + '!' for sentence in sentence_list]
        return sentence_list