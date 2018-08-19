'''
Write a program, which will find all the numbers between 1000 and 3000 (both
included) such that each digit of a number is an even number. The numbers
obtained should be printed in a comma separared sequence on a single line.
'''

for i in range(1000, 3001):
    number = str(i) # Convert i into string
    if int(number[3]) % 2 == 0: # convert number intp int
        if int(number[2]) % 2 == 0:
            if int(number[1]) % 2 == 0:
                if int(number[0]) % 2 == 0:
                    print(number, end = ',')
