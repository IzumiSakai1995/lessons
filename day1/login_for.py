#__author: Liu Zheng
#date:2018/6/20


_user = 'LZ'
_passwd = 'abc123'
passed_authentication = False

for i in range(3):
    username = input('Username:')
    password = input('Password:')

    if username == _user and password == _passwd:
        print("Welcome %s login.....",username)
        passed_authentication = True
        break
    else:
        print('Invalid username or password !')
else:
    print('wrong')
