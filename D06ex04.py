names_e = []

file_handle = open('roster.txt','r')
file_lines = file_handle.readlines()
for i in file_lines:
    if 'e' in i.split()[0]:
        names_e = names_e + [str(i.split()[0])]
file_handle.close()
f = open('Names_with_e.txt', 'w')
for i in names_e:
    f.write(i+"\n")
f.close()
