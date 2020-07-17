cat =['a','b','d']

appy=cat[0]
ball=cat[1]
dd = cat[2]

# Irrespective of first one we can do this one:

appy, ball, dd = cat

print(appy, ball, dd)



# swaping values trick
a=10
b=100

a,b = b, a

# Some inbuilt function of list

#  index()
list1=[12,14,121]
print(list1.index(14))

# append() method
list1.append(2)
print(list1)


# insert method 

list1.insert(1, 'new value')
print(list1)