# create while loop to help speed up development
# the user should be able to enter a number or word
# calculate the length of that word or number
# If the length number is greater than 2 have it do some calculations
# If the length number is less than or equal to 2 have it do some other calculations
from custom_funcs import *

replay = "y"
while (replay == "y"):
    print("\n\tHello and Welcome to Random Calculations!")
    user_input = str(input("\n\tPlease enter any numbers, words, or characters here..."))
    user_input = len(user_input)

    if user_input <= 2:
        less_equal_two(user_input)
    elif user_input > 2:
         greater_two(user_input)

    replay = str(input("\n\tWould you like to rerun this program (y/n)..."))
    replay = replay.lower()
exit()
