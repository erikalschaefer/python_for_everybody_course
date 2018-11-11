"""First Chapter 10 assignment on tuples"""

file_handle = open ('mbox.txt')
my_dict = {}
for line in file_handle:
    words = line.split()
    line = line.lower
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    email_address = words[1]

    my_dict[email_address] = my_dict.get(email_address, 0) + 1
print (my_dict)


my_list = list()
for key, val in list(my_dict.items()):
    my_list.append((val, key))
    
my_list.sort(reverse=True)

print ('-----------------My List is Below ------------------------------------------')

for key, val in my_list[:10]:
    print (key, val)