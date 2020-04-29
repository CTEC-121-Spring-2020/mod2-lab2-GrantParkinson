"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


#from math import *




import math
def main():
    '''
    my_string = "hello"
    print(my_string)
    print(type(my_string))
    my_int = 33
    print(my_int)
    print(type(my_int))
    print()
    print("math demo formula")
    r = 3
    v = (4/3)*pi*r**3
    print("v:", v)

    print()

    # Get a string
    aString = input("Enter a string of characters: ")
    print(aString)

    # Print 2 blank lines
    # print("\n\n")

    # Get an integer
    # Int does not accept float inputs or non numeric string inputs
    myInt = int(input("Enter a number: "))
    print(myInt)

    # Print 2 blank lines
    # print("\n\n")

    # Get a floating point number
    myFloat = float(input("Enter a number (decimals are ok): "))
    print(myFloat)

    # Print 2 blank lines
    # print("\n\n")

    # Evaluate an expression entered
    # Enter 3+4
    aNumber = eval(input("Enter a number or a numeric expressions: "))
    print(aNumber)

    # Print 2 blank lines
    # print("\n\n")

    x, y = eval(input("Enter two numbers separated by a comma: "))
    print(x, y)
    print(type(x))
    print()

    x, y = input("provide two values: ").split()
    print(x, y)
    print(type(x))
    x = int(x)
    y = int(y)
    print(type(x))
    print(type(y))
    print()

    # demo definite loops
    for i in [10, 1, 2, 3]:
        print(i)
    print()
    for count in range(4):
        print(count)
    print()
    for i in range(0, 40, 5):
        print(i)

    # Math library use
    print(math.pi)
    print(math.sqrt(4))
    print(math.ceil(math.pi))
    print(math.floor(math.pi))

    sum = 0
    for i in [56, 19, 92, 56]:
        sum = sum + i
    print(sum)
    '''
    # get input and accumulate a sum
    sum = 0
    for i in range(5):
        input_value = eval(input("Enter a number: "))
        sum = sum + input_value
    print("sum: ", sum)
    print()


main()
