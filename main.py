# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# importing random module
import random

# function to check the Guess
def check_guess(rand_num):

    while True:
        # User input
        num = int(input("Guess a number : "))

        # Check User Guess with random number
        if num == rand_num:
            print("Hurray, Your Guess is right, you are awesome!!!")
            break
        else:
            print("Sorry, Your guess is wrong, Please Try again!")
            print("BEST OF LUCK FOR NEXT TIME")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("*****Guessing Game Application*****")

    # Generate Random Number
    rand_num = random.randint(1, 100)
    print("Random Number is : ",rand_num)

    # Call Function
    check_guess(rand_num)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
