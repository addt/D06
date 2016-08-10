#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def has_no_e(wrd):
    if 'e' in wrd:
        return True
    else:
        return False

def print_no_e():
    file_handle = open('roster.txt','r')
    file_lines = file_handle.readlines()
    count = 0
    for i in file_lines:
        if 'e' in i:
            count += 1
    file_handle.close()
    return str((count/len(file_lines) * 100))

##############################################################################
def main():
    print(has_no_e("avi"))
    print(has_no_e("python"))
    print(has_no_e("testing"))

    lst_with_e = ["testing", "avi", "asus", "android"]
    lst_without_e = ["dixit", "addt", "htc"]
    print(print_no_e())

if __name__ == '__main__':
    main()
