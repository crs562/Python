'''
Design a code which will find the given number is Palindrome number or not.
'''

input_number = input("Enter a number: ")

try:
    value = int(input_number)
    if input_number == str(input_number)[::-1]:
        print(input_number, "is is Palindrome number")
    else:
        print(input_number, "is not Palindrome number") 

except ValueError:
    print(input_number, "is not a number")
