pets = {
    'tom' : {
        'first_name':'aa',
        'last_name':'bb',
        'age':18,
        'city':'beijing'
        },
    'jerry' : {
        'first_name': 'cc',
        'last_name': 'dd',
        'age': 78,
        'city': 'shanghai'
        },
}
for username,user_infos in pets.items():
    print("name " + username)
    for user_info in user_infos.values():
        print(user_info)