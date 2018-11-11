"""Second Chapter 10 assignment on tuples"""

file_handle = open ('mbox-short.txt')
my_dict = {}
for line in file_handle:
    words = line.split()
    line = line.lower
    if len(words) == 0: 
        continue
    if words[0] != 'From': 
        continue

    day_of_week = words[5]
    day_of_week = day_of_week.split(':')

    hour = day_of_week[0]

    my_dict[hour] = my_dict.get(hour, 0) + 1


#This will sort my dictionary 
my_list = list()
for key,val in list(my_dict.items()):
    my_list.append((key,val))

    
my_list.sort(reverse=False)



print ('---------------my list is below-----------------------------')

for key,val in my_list[:]:
    print (key,val)
