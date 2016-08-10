#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body


def avoids(wrd, forbidden_letters):
    for i in forbidden_letters:
        if i in wrd:
            return False
    return True


def forbidden_prompt():
    forbidden_letters = input("Enter forbidden letters")
    return forbidden_param(forbidden_letters)    


def forbidden_param(letters):
    file_handle = open('words.txt','r')
    file_lines = file_handle.readlines()
    count = len(file_lines)
    excl_words = []
    for i in file_lines:
        for j in letters:
            if j in i:
                count -= 1
                #excl_words = excl_words + [i]
                break
    file_handle.close()
    return count
                
        
    

def find_five():
    letter_list = "abcdefghijklmnopqrstuvwxyz"
    letter_list_count = []
    excl_words = []
    for i in letter_list:
        #print(forbidden_param(i))
        #(num, count) = forbidden_param(i)
        letter_list_count = letter_list_count + [[forbidden_param(i),i]]
        #excl_words = excl_words + count
        #[[int(forbidden_param(i)), i]]
    min_exclusion_list = []
    for j in range(1,6):
        min_exclusion = min(letter_list_count)
        letter_list_count.remove(min_exclusion)
        min_exclusion_list = min_exclusion_list + [min_exclusion]
    return min_exclusion_list   
        
        
    
##############################################################################
def main():
    #list_letters = [['a',0], ['b',0], ['c',0]]
    #print(forbidden_param("abcdefghijklmnopqrstuvwxyz"))
    print(find_five())


if __name__ == '__main__':
    main()
