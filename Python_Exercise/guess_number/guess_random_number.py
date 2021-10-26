import random


def guess_random_numbers():
    global userInput, guesses_taken
    guess_number = random.randint(1, 10)
    print('Welcome to lois guessing game. ')
    for guesses_taken in range(1, 5):
        userInput = int(input('Take a guess from numbers between 1 - 10.\n'))

        if userInput > guess_number:
            print('Your guess' + str(userInput) + ' is too high')
        elif userInput < guess_number:
            print('Your guess' + str(userInput) + ' is too low')
        else:
            break

    if userInput == guess_number:
        print('Congratulation your guess ' + str(guesses_taken) + 'guesses')
    else:
        print('well done on your effort please try again the actual guess number is ' + str(guess_number))


guess_random_numbers()