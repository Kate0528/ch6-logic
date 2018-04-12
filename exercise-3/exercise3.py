import random
def print_hot_or_cold(target,guess):
    if(guess==target):
        print("got it!")
    elif (abs(guess-target)<=1):
        print("scalding hot")
    elif(abs(guess-target)<=3):
        print("very warm")
    elif(abs(guess-target)<=5):
        print("warm")
    elif(abs(guess-target)<=8):
        print("cold")
    elif(abs(guess-target)<=13):
        print("very cold")
    else:
        print("icy freezing miserably cold")
    if (guess >target):
        print("guess is high")
    elif(guess ==target):
        print("guess is equal to target")
    else:
        print("guess is low")
# Define a function `guess_number()` that takes a single argument (a target number)
# and prompts the user for a guess using the `input()` method. Your function should
# then print how close the user's guess is to that target (use your previous 
# function!). Note that you will need to convert the input into a number.


# Once you have a single guess working, modify your function so that the user can
# make MULTIPLE guesses. You can either do this using a loop (see the next chapter)
# or by simply calling your `guess_number() method again IF the user didn't get
# the answer right. The later is an example of **recursion**.

def guess_number(target):
    guess=int(input("Please guess a number"))
    print_hot_or_cold(target,guess)
    if(target!=guess):
        guess_number(target)   


# If the file is run as a top-level script, your script should pick a random number
# between 1 and 50 as the target and then start the game. You should inform the
# user of the range of numbers before asking them for a guess.
if __name__ == "__main__":
    print('The random number is between 1 and 50')
    guess_number(random.randint(1,51))