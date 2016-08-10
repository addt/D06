names_e = []

file_handle = open('roster.txt','r')
file_lines = file_handle.readlines()
for i in file_lines:
    if 'e' in i.split()[0]:
        names_e = names_e + [i.split()[0]]
file_handle.close()
print(names_e)
