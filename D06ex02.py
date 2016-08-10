import random

f = open('random_no.txt', 'w')
for i in range(0,10):
    input_no = random.randint(1,1000)
    f.write(str(input_no)+"\n")
f.close()
    
