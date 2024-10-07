# Modifying Dictionaries

'''
Dictionaries are a mutable data structure so you are able to modify them..

#  Adding an changing dictionary elements::

without using a function you can add key value pairs to dictionaries by using the following syntax:::
'''

sammy={'username':'sammy-shark','online':True, 'followers': 987}

# print(sammy)

username = {'sammy': 'sam-shark','jermie':'dhfkjdhf'}

username ['Drew']= 'squidly'

# print(username)

# usernames.py

# define original dictionary

usernames= {'sammyy': 'Diablo','will': 'rosty'}

while True:

    print('Enter a name:')

    name =input()
    
    if name in usernames:
        print(usernames[name] + ' is the username of ' + name)

    else:


        print('I don \'t have '  + name  +'\'s username, what is it ?' )

    username=input()

    usernames[name] =username

    print('Data updated..')


