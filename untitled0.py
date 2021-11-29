#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:24:21 2021

@author: pabloquihui
"""


palindrome = 0
split_strings = []
split_strings2 = []
base = []
base_comp = []
txt_input = open("Test.txt","r")
content = txt_input.read()
min_len = int(input("Enter minimum length of palindromes: "))

def split(content,min_len):
    for i in range(0, len(content), (min_len)):
        split_strings.append(content[i : i + (min_len)])
    return split_strings

def list_bases(split_strings):
    for r in range(0, len(split_strings)):
        base.append(list(split_strings[r]))
        base_comp.append(list(split_strings[r]))
    return base, base_comp


def comp(base):
    for k in range(0, len(base)):
        for x in range(0, len(base[k])):
            y = base[k][x]
            if y == str('A'):
                base_comp[k][x] = 'T'
            if y == 'G':
                base_comp[k][x] = 'C'
            if y == 'C':
                base_comp[k][x] = 'G'
            if y == 'T':
                base_comp[k][x] = 'A'
    return base_comp

def reverse(base_comp):
    base_comp_re = base_comp
    for q in range(0,len(base_comp)):
        base_comp_re[q].reverse()
    return (base_comp_re)

def check(base,base_comp_re):
    palindrome = 0 
    for w in range(0,len(base)-1):
        for j in range(0,len(base_comp_re)-1):
            if base[w] == base_comp_re[j+1]:
                palindrome = palindrome + 1
    return (palindrome)


base = list_bases(split(content, min_len))[0]
print(base)
base_comp = comp(base)
print(base_comp)
base_comp_re = reverse(base_comp)
print(base_comp_re)

    
if check(base,base_comp_re) == 0:
    
    for i in range(0, len(content), (min_len)):
        if i == 0:
            split_strings2.append(content[i : i + (min_len)])
        else: 
            split_strings2.append(content[i+1 : i + (min_len)+1])
    base = []
    base_comp = []
    base = list_bases(split_strings2)
    base_comp = comp(base)
    base_comp_re = reverse(base_comp)
    print(base_comp)
    print(check(base,base_comp_re))
    
else:
    print(check(base,base_comp_re))
#print(check(base,base_comp_re))

    
#max_len = input("Enter maximum length of palindromes: ")

