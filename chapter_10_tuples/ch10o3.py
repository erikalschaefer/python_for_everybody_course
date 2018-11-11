"""Chapter 10-3 practice - print out the 10 most common words in the text file"""

import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    print (line)

    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)