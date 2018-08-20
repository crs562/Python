'''
A website requires a user to input username and password to register. Write a program
to check the validity of password given by user. Following are the criteria for checking
password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
'''

password = input("Enter your password: ")

small_char = 0
number = 0
large_char = 0
special = 0
output = "output"
for i in password:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        small_char = small_char + 1
    elif i in '0123456789':
        number = number + 1
    elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        large_char = large_char + 1
    elif i in '$#@':
        special = special + 1
    else:
        output = "Invalid Password"
        break

if (small_char >= 1 and number >= 1 and large_char >= 1 and special >= 1 and (6 <= len(password) <= 12)):
    print("Valid Password")
elif output == "Invalid Password":
    print("Invalid Password")
else:
    print("Invalid Password")
