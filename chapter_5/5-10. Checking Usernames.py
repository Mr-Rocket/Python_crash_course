current_users = ['Admin', 'lasha', 'nikoloz', 'gela', 'bela']
new_users = ['admin', 'LASHA', 'nikoloz', 'gela1', 'bela']



print('\n checking users: \n')

for user in new_users:
    # print(user)
    if user.title() in current_users and user.lower() in current_users:
        print(f'user {user.title()} is already taken')
    else:
        print(f'username {user.title()} is available')


