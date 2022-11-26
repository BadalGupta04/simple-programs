# Write a python program to find out if a given number is even or odd using a user defined function.
#
# num = int(input("Enter a number :"))
# if (num % 2) == 0:
#     print("The no. is even")
# else:
#     print("The no. is odd")


def cloudy(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


x = int(input("Enter a number"))
cloudy(x)
