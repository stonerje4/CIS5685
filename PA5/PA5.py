###James Stoner
###PA5
###3/1/2023

import string 


f = open("python homework\PA5\PA5.txt", 'r')
file = f.readlines()

mylist = []

for line in file:
    line = line.translate(str.maketrans('', '', string.punctuation)).lower()
    line = line.split()
    for word in line:
        mylist.append(word)

print(len(mylist))


    