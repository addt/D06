# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(lst):
    count = 0
    for i in lst:
        #print(count)
        if isinstance(i, int):
            count = count + i
        else:
            count = count + nested_sum(i)
    return count


def main():
    ltt = [[4,5,[1,2,3]],1,2,3,4,5,[3,2,1]]
    print(nested_sum(ltt))

if __name__ == '__main__':
    main()
        
