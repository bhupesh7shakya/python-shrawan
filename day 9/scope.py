# x=10

# def hello():
#     global x
#     x=9
    
    
    

# print(x)
# hello()
# print(x)


# task
# is_Login global variable
# default value chai False

# login function
# takes two parameter username and password
# create a constanct variable two USERNAME and PASSWORD with default value 
# login check 
# is_Login global update True
# LIST_OF_USER ko dictionary
# [{
    # "username":"fsdf",
    # "password":"password"
# }]


is_Login=False

def login(username,passsword):
    USERNAME='test'
    PASSWORD='password'
    if username==USERNAME and passsword==PASSWORD:
        global is_Login
        is_Login=True
        
        
print(is_Login)
login('test','passsword')
print(is_Login)
        