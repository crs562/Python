'''
Write a program that accepts a sentence and calculate the number of letters and
digits.
'''

input_string = input("Enter a String: ")

digit = letter = 0
for i in input_string:
    if i.isdigit():
        digit = digit + 1
    elif i.isalpha():
        letter = letter + 1
    else:
        pass

print("Letters: ", letter)
print("Digits: ", digit)
