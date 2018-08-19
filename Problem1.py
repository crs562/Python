'''
Write a program which will find factors of given number and find whether the
factor is even or odd.
'''

input_number = input("Enter a number: ")

try:
    number = int(input_number)

    print("Factor of a number associated with Odd/Even")
    for i in range(1, number + 1):
        if (number % i == 0):
            if (i % 2 == 0):
                print(i, "even")
            else:
                print(i, "odd")

except ValueError:
    print(input_number, "is not a number")
