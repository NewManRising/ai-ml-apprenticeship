import random

#---------------------------------------------------------#

# Comparisons:
# Equal:             ==
# Not Equal:         !=
# Greater Than:      >
# Less Than:         <
# Greater or Equal:  >=
# Les or Equal:      <=
# Object Identity    is

# and
# or
# not

# False values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence, Ex, '', (), [].
    # Any empty mapping. Ex, {}.



print("Welcome!\n")

number = random.SystemRandom()


while True:
    ask_age = input("What is your age? ")
    try:
        age = int(ask_age)
        if age < 18:
            print("You are a minor")
        else:
            print("You are an adult")
        break
    except ValueError:
        print("Please enter a number")



adult = True
senior = 65

if adult and age >= senior:
    print("You are a senior")



pick_num = number.randint(1, 10)

while True:
    user_input = input("Guess a number between 1 and 10 (press q to quit): ")
    if user_input.lower() == 'q':
        print("Quitting - Goodbye!")
        break

    try:
        guess = int(user_input)
        if guess < 1 or guess > 10:
            print("Please choose a number between 1 and 10")
        elif guess == pick_num:
            print("You guessed correctly!")
        else:
            print("You guessed incorrectly!")
    except ValueError:
        print("Type a valid number")




