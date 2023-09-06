def star(func):
    def wrapper():
        print("*" * 10)
        func()
        print("*" * 10)
    return wrapper


def hash(func):
    def wrapper():
        print("#" * 10)
        func()
        print("#" * 10)
    return wrapper

# dollar
# @hash
# @star
def hello_world():
    print("hello world")
    
# @hash
def hello():
    print("hello")
    
hello_world()
hello()




# hash(hello)()
hash(star(hello_world))()


# hello_world()
# hello()
# ##########
# **********
# hello world
# **********
# #########

# ##########
# hello
# ##########