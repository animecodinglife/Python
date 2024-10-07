# Using Function to ACCESS elements

'''
in addition to using keys to access values we can also work some built function dict.keys() isolate keys- dict.values() isolates values -dict.items() returns in a list format of(key, value tuple pairs)

'''

sammy1={'username':'sammy-shark','online':True, 'followers': 987}


# print(sammy1.keys())

sammy2={'username':'sammy-shark','online':True, 'followers': 987}
jess={'username': 'dlkjfsf', 'online': False,'points':9898}

# for common_key in sammy2.keys() & jess.keys():
    # print(sammy2[common_key], jess[common_key])


sammy={'username':'sammy-shark','online':True, 'followers': 987}

# print(sammy.values())

# print(sammy.items())

for key, value in sammy.items():
    print(key, 'is the key for the value', value)