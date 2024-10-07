# DELETING Dictionary Elements

'''
Just as you can add key-value pairs and change values within the dictionary data type, you can also delete items within a dictionary..

del dict[key]

'''

# Let's take the jesse dictionary that represents one of the users,, says that jesse is no longer using the online platform for playing games so well remove the items associated with the points key...


jess={'username': 'Jocsit','online':False,'points': 877,'follower': 69876}

# del jess['points']

jess.clear() #If we would like to clear a dictionary of all of its values we can do so with the dict.clear() function..

del jess #If we no longer need a specific dictionary we can use del to get rid of it entirely:::
        # after deleting the jesse dictionary we'll recieve the following error::
print(jess)
