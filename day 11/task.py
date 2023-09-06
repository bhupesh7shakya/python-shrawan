user_list=[]


def user_exits(email):
    for user in user_list:
        if user.get('email')==email:
            print("User email alredy exits")
            return True
    return False
    

def register(email,password):

    if not user_exits(email):
        user={
            'email':email,
            'password': password
        }
        user_list.append(user)


def login(email,password):
    for user in user_list:
        if user.get('email')==email and user.get('password')==password:
            print("You have been Logged int")
            return True
    print("Credential don't match")
    return False

def show_users():
    for user in user_list:
        print(f"email|password")
        print(f"{user['email']}|{user['password']}")
  
is_Login=False

while True:
    choice=input("""
                 press 1 to register
                 press 2 to login
                 """)
    if choice=="1" or choice =="2":
        
        email=input("Enter the Email")
        password=input("Enter the Password")
    
    if choice == "1":
        register(email,password)
    elif choice == "2":
        
        is_Login=login(email,password)
    
    else:
        if is_Login==True:
          show_users()
        else:
            print("You must login first")