

# task
# list of fruit(argument) bich vegetable
# pring only fruites
def fruit(*fruits):
    for fruit in fruits:
        if fruit != "tomato":
            print(fruit)
# fruits=[]
# for i in range(3):
#     fruit[i]=input("enter any Fruits")
    
# fruit(fruits)

# args
# def sum(*numbers):
#     total=0
#     for num in numbers:
#         total+=num
#     return total


# total_sum=sum(1,2,3)
# print(total_sum)

# biography
# name
# age
# course enabl
#addres etc..... 



# def person(**person):
#     print(person['name'],person['middle_name'],person['last_name'])
    
# person(name="ram",last_name="somethign")


# recursions
# task
# range function recreate 
# homework

# def number(num=0):
#     print(num)
#     if num ==10:
#         return 
#     number(num+1)

# number()

# print(list(range(5,10,2)))


# x=lambda a:a+1

# print(x(2))

def myfunc(n):
    return lambda a:a*n

# lambda a:a*2
doubler=myfunc(2)

# lambda a:a*10
# tripler=myfunc(10)
# print(doubler(10))
# print(tripler(3))