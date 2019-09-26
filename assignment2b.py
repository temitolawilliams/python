name_entered = input('Enter user names:')

users_name_list = ['Tola ogundare','Yomi ogundare','Fisayo ogundare','obafemi ogundare','dupe ogundare', 'olabisi olaitan']

if name_entered in users_name_list:
    print('Name is in the list, access granted!')
else:
    print('Name not in the list, access denied!!')