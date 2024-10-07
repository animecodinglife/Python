# slicing Tuple:: We can use indexing to call out a few items from the tuple. Slices allow us to call multiple value by creating a range of index numbers separated by a colon [x:y]..

coral =('blue coral','strugeoun','loch ness','killer whale','greenland shark','Six gill sharks')
'''
print(coral[1:4])
print(coral[::2])
print(coral[-5:-1:2])
print(coral[0:5])
'''

# The syntax for the constructions is tuple [x:y:z] with referring to stride let's make a larger lists then slice it and give the stride a value of 2::

number =(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

print(number[1:18:4])

print(number[::3])