favorite_numbers = {
    'alex': ['1', '3'],
    'bob': ['12', '6'],
    'chris': ['32', '23'],
    'dave': ['52', '43'],
    'eva': ['99']
}
for user, user_info in favorite_numbers.items():
    if len(user_info) > 1:
        print(f"{user.title()}'s numbers are")
        for element in user_info:
            print(element)
    else:
        print(f"{user.title()} have only one number:{user_info}")