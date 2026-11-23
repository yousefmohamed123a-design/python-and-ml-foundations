# validate user input exercise
"""
1.username is no more than 12 characters
2.username must not contain spaces
3.username must not contain digits
"""

user_name = input("Enter your username : ")

test1 = len(user_name)
test2 = user_name.find(" ")
test3 = user_name.isalpha()

if test1 > 12:
    print("Username is not valid !")
    print("Username must not contain more than 12 charachters")
elif test2 != -1:
    print("Username is not valid !")
    print("Username must not contain spaces")
elif not test3:
    print("Username is not valid !")
    print("Username must not contain digits")
else:
    print("Username is valid !")
    print(f"Welcome {user_name}")
