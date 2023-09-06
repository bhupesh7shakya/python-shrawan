# person={
#     "first_name":"ram",
#     "last_name": "kumar",
#     "first_name":"rfsdkafhjm",
#     "courses":[
#         "math",
#         "python",
#     ]
    
# }

# print(person["courses"][1])
# python reverse print


# name="ram"
# age=12


# my name is ___ and and is ___
# print(f"my name is {name} and age is {age}")

# print("my name is "+name+"and age is",age)

# create a dictionary with variable name =human
# 

# print
# my name ____ and 
# i am currenlty studying ___
# 1.sdafsd
# 2.sdfasdfsadf
# 3.fjaskdfjkl
# and 
# my familiy member are
# 1.name(relation)
# 2.name(relation)
# 3.name(relation)
# 4.name(relation)

human=[
    {
    "name":"ram",
    "course":"python",
    "hobby":[
        "a",
        "b",
        "c",
    ],
    "family_member":[
        {
            "name":"a",
            "relation":"father",
        },
        {
            "name":"b",
            "relation":"mother",
        },
        {
            "name":"c",
            "relation":"sister",
        },
        {
            "name":"d",
            "relation":"brothers",
        },
    ]
},
 {
    "name":"shyam",
    "course":"python",
    "hobby":[
        "a",
        "b",
        "c",
    ],
    "family_member":[
        {
            "name":"a",
            "relation":"father",
        },
        {
            "name":"b",
            "relation":"mother",
        },
        {
            "name":"c",
            "relation":"sister",
        },
        {
            "name":"d",
            "relation":"brothers",
        },
    ]
},      
]

print(f"""
My name is {human[0]['name']} and
I am currently learning {human[0]['course']}.
1.{human[0]['hobby'][0]}
2.{human[0]['hobby'][1]}
3.{human[0]['hobby'][2]}
and 
my familiy member are
1.{human[0]['family_member'][0]['name']}({human[0]['family_member'][0]['relation']})
2.{human[0]['family_member'][1]['name']}({human[0]['family_member'][1]['relation']})
3.{human[0]['family_member'][2]['name']}({human[0]['family_member'][2]['relation']})
4.{human[0]['family_member'][3]['name']}({human[0]['family_member'][3]['relation']})

    """)

print(f"""
My name is {human[1]['name']} and
I am currently learning {human[1]['course']}.
1.{human[1]['hobby'][0]}
2.{human[1]['hobby'][1]}
3.{human[1]['hobby'][2]}
and 
my familiy member are
1.{human[1]['family_member'][0]['name']}({human[1]['family_member'][0]['relation']})
2.{human[1]['family_member'][1]['name']}({human[1]['family_member'][1]['relation']})
3.{human[1]['family_member'][2]['name']}({human[1]['family_member'][2]['relation']})
4.{human[1]['family_member'][3]['name']}({human[1]['family_member'][3]['relation']})

    """)

# ctrl+d for sametype selection
# ctrl+shift+down_arrow duplicate tala tira
# ctrl+alt+down_arow select same col antoher row 

# ctrl+h to find and replace

# to replace on selected lines
# alt+l