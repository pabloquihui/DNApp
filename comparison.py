import re
import sys
import os

file_wuhan = open("wuhan.txt", "r")
file_delta = open("delta.txt", "r")

wuhan_lines = file_wuhan.readlines()
delta_lines = file_delta.readlines()
f = open("wuhan_delta_comparison_2.txt", "a")
x = 0
common = list()
for i in range(len(wuhan_lines)):
    for j in range(len(delta_lines)):
        if wuhan_lines[i] == delta_lines[j]:
            palindrome = wuhan_lines[i]
            palindrome.replace("\n", "")
            print(palindrome)
            if palindrome not in common:
                common.append(palindrome)
                f.write(f"Palindrome {common[len(common)-1]} from Wuhan Reference is in Delta Variant")
                f.write("\n")
                print(common)
                x += 1
print(x)            
f.write(f"Total number of palindromes found in common: {len(common)}")
f.close()
