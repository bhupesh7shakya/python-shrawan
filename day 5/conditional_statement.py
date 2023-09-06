is_Login=False
is_Authorize=False

if is_Login and is_Authorize:
    print("secret data")
elif is_Login:
    print("basic data")
else:
    print('user not loggedin')