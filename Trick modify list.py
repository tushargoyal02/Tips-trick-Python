# In this part we will look how to create a copy of list without reference


# lets see

animals=['tiger','lion','rat']

print(animals)

bird = animals

bird[0]='sparrow'
print(bird)
print(animals)            # here the same changes are seen in both the list


# Making a copy of list

import copy

scr = [1,2,3,4,5]

chr1 = copy.deepcopy(scr)

chr1[0] = 0000

print('chr1:',chr1)

print('scr', scr)




# dict.get('check key','return if not found') :
    # get function is used to return value if found in dict or any other message you want

dict1 = {1:'a', 2:'b'}
print(dict1)

# retrieve value according to key
print(dict1.get(1,'bello'))

# give any message if key not found
print(dict1.get(111,'hell!!! nothing found'))


# .setdefault() method is used to set key, value pair if not present
dict1.setdefault('baba',12)

print(dict1)

# trying to update more value
dict1.setdefault('baba',121212)
print(dict1)