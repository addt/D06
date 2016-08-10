#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:ooh ah aah    
#       2: allheal loofah
#       3: ho fellah
##############################################################################
# Imports

# Body
def uses_only(word, letters):
    for i in word:
        if i not in letters:
            return False
    return True

def create_sentence(letters):
    valid_words = []
    file_handle = open('words.txt','r')
    file_lines = file_handle.readlines()
    for i in file_lines:
        if uses_only(i.strip(), letters):
            valid_words = valid_words + [i.strip()]
    print(valid_words)
        

##############################################################################
def main():
    print(uses_only('avidixit','avidixitasdasdasdasdasd'))
    print(create_sentence('acefhlo'))
if __name__ == '__main__':
    main()
