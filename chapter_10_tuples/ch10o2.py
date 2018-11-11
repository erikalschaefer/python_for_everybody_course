"""Chapter 10-2 practice on creating a dictionary and sorting by the value of key-value pair."""


my_dict = {'a' : 10, 'b' : 1, 'c' : 22}

my_list = list()

for key, val in my_dict.items() :
    my_list.append ( (val, key) )
    print (val, key)

my_list.sort(reverse=True)
print ('This is a list with the value listed first and the key listed second', my_list)