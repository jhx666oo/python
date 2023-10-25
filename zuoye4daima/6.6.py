favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['jen', 'sarah', 'edward', 'phil', 'alex', 'dave', 'chris']
for name in favorite_languages.keys():
    if name in friends:
        print(f"Thank you,{name.title()}")
        friends.remove(name)
for friend in friends:
    print(f"Dear {friend.title()},please join in")